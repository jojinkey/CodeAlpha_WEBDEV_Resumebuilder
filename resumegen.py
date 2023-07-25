from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the route for the resume form
@app.route('/resume_form', methods=['GET', 'POST'])
def resume_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        education = request.form['education']
        internship = request.form['internship']
        experience = request.form['experience']
        projects = request.form['projects']
        leadership_activities = request.form['leadership_activities']
        skills = request.form['skills']

        # Generate the PDF resume
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
        pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
        pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True)
        pdf.cell(200, 10, txt=f"Education:\n{education}", ln=True)
        pdf.cell(200, 10, txt=f"Internship:\n{internship}", ln=True)
        pdf.cell(200, 10, txt=f"Experience:\n{experience}", ln=True)
        pdf.cell(200, 10, txt=f"Projects:\n{projects}", ln=True)
        pdf.cell(200, 10, txt=f"Leadership and Activities:\n{leadership_activities}", ln=True)
        pdf.cell(200, 10, txt=f"Skills:\n{skills}", ln=True)

        # Add other fields to the PDF here

        # Save the generated PDF in the 'generated_resumes' folder
        folder_name = "generated_resumes"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_path = os.path.join(folder_name, f"{name}_resume.pdf")
        pdf.output(file_path)

        return render_template('resume_generated.html', file_path=file_path)

    return render_template('resume_form.html')

# Define the route to download the generated resume
@app.route('/download_resume')
def download_resume():
    # Generate the resume and get the filename
    filename = generate_resume()

    # Send the generated resume as an attachment for download
    return send_file(filename, as_attachment=True)

# Function to generate the resume and save it in PDF format
def generate_resume():
    # ... (code to get user details and generate the resume)

    # Example code to generate a simple PDF resume using FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Your Resume Content Goes Here!", ln=True, align="C")
    filename = "ok_resume.pdf"  # You can create a unique filename based on user details

    # Create the "generated_resumes" folder if it doesn't exist
    if not os.path.exists("generated_resumes"):
        os.makedirs("generated_resumes")

    # Save the PDF in the "generated_resumes" folder
    pdf.output(os.path.join("generated_resumes", filename))
    return os.path.join("generated_resumes", filename)

if __name__ == '__main__':
    app.run(debug=True)
