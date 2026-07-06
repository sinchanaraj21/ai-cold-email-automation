from excel_reader import load_hr_data
from email_generator import generate_email

df = load_hr_data()

html = generate_email(df.iloc[0])

print(html)