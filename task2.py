import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

data = {
    "Student": ["Amit", "Neha", "Rahul", "Priya"],
    "Marks": [78, 85, 67, 92]
}

df = pd.DataFrame(data)
df.to_csv("student_data.csv", index=False)

df = pd.read_csv("student_data.csv")

average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

pdf = SimpleDocTemplate("Student_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("Automated Student Performance Report", styles["Title"]))
elements.append(Paragraph(f"Average Marks: {average_marks:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Marks: {highest_marks}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Marks: {lowest_marks}", styles["Normal"]))

table_data = [df.columns.tolist()] + df.values.tolist()
table = Table(table_data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(table)
pdf.build(elements)
