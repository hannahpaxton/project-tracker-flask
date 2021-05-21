"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-creation-form")
def student_add_form():
    """Form to add a student."""

    return render_template("student_creation_form.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add student."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student_added.html", github=github)


@app.route("/project")
def get_project_grade():
    """Show information about a project grade."""

    title = request.args.get('title')

    title, description, max_grade = hackbright.get_project_by_title(title)

    html = render_template("project_info.html",
                           title=title,
                           description=description,
                           max_grade=max_grade)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
