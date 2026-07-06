from excel_reader import load_hr_data
from email_generator import generate_email

df = load_hr_data()

hr = df.iloc[0]

html = generate_email(hr)

print(html)