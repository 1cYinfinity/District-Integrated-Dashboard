# Import Necessary Libraries

from flask import Flask, render_template

app = Flask(__name__)

# Here we're using some sample data for our projects.

project = [
   {
      'name': 'Road Construction',
      'department': 'Public Works',
      'progress': 70,  
   },
   {
      'name': 'Healthcare Expansion',
      'department': 'Health',
      'progress': 90,  
   },
]

schemes = [
  {
      'name': 'Education Enhancement',
      'department': 'Education',
      'progress': 60,  
  },
  {
        'name': 'Agriculture Development',
        'department': 'Agriculture',
        'progress': 75,
    },
]

@app.route('/')
def dashboard():
  return render_template('dashboard.html' , projects=projects , schemes=schemes)

if __name__== '__main__':
  app.run(debug=True)
