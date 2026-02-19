import pandas as pd
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

csv_path = "/Users/dimitricromarty/Downloads/SA CEA Student Listing Spring 2026.csv"
output_path = "/Users/dimitricromarty/Downloads/Grouped_Email_List.pdf"

email_column = "All Institutional Email Addresses"
program_column = "Primary Program of Study"
chunk_size = 50


def clean_email(email):
    email = str(email).strip().lower()
    email = re.sub(r'\s+', '', email)
    return email

def main():
    # Load CSV
    df = pd.read_csv(csv_path, encoding="latin1")

    # Drop rows without program or email
    df = df.dropna(subset=[email_column, program_column])

    # Clean emails
    df[email_column] = df[email_column].apply(clean_email)

    # Remove duplicates just in case
    df = df.drop_duplicates(subset=[email_column])

    # Sort by program then email
    df = df.sort_values(by=[program_column, email_column])

    # Group by program
    grouped = df.groupby(program_column)

    # Create PDF
    doc = SimpleDocTemplate(output_path)
    elements = []

    styles = getSampleStyleSheet()
    header_style = styles["Heading1"]
    text_style = styles["Normal"]

    for program, group in grouped:
        elements.append(Paragraph(str(program), header_style))
        elements.append(Spacer(1, 0.3 * inch))

        emails = list(group[email_column])

        # Break into chunks of 50
        for i in range(0, len(emails), chunk_size):
            chunk = emails[i:i + chunk_size]
            email_line = ";".join(chunk)
            elements.append(Paragraph(email_line, text_style))
            elements.append(Spacer(1, 0.25 * inch))

        elements.append(PageBreak())

    doc.build(elements)

    print(" PDF successfully created at:")
    print(output_path)


if __name__ == "__main__":
    main()
