from flask import Flask, request, redirect
import csv

app = Flask(__name__)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Extracting data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    referrer_url = request.referrer

    # Define the CSV file name
    csv_file = 'submissions.csv'

    # Writing data to the CSV file
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header only if the file is new
        if file.tell() == 0:
            writer.writerow(['Name', 'Email', 'Message', 'Referrer URL'])
        writer.writerow([name, email, message, referrer_url])

    # Redirect back to the referring page
    return "Succesfully submitted form! Thank you and RedeemedGPT will contact you ASAP"

if __name__ == '__main__':
    app.run(debug=True)
