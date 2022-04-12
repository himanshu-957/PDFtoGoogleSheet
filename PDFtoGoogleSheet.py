import camelot
from oauth2client.service_account import ServiceAccountCredentials
import gspread
tables = camelot.read_pdf('pdfdoc.pdf', pages = '1', flavor = 'stream')
##tables
##<TableList n=1>
tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 2
}
##tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
df2=tables[0].df # get a pandas DataFrame!pip install "camelot-py[cv]"pip install "camelot-py[]"
print(df2)
scope = {"https://www.googleapis.com/auth/spreadsheets",
  "https://www.googleapis.com/auth/drive.file",
  "https://www.googleapis.com/auth/drive"}
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json",scope)
client = gspread.authorize(creds)
python_test = client.open("minor2").worksheet("Sheet1")
python_test.append_rows(df2.values.tolist())
