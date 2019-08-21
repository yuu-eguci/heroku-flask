<!DOCTYPE html>
<html>
  <head>
    <title>flask demo app</title>
  </head>
  <body>
    <form action="{{ url_for('add_entry') }}" method=post>
      <input type="text" name="title">
      <input type="text" name="text">
      <input type="submit">
    </form>
    <ul class="entries">
    {% for entry in entries %}
      <li>{{entry.title}} / {{entry.text}}</li>
    {% endfor %}
    </ul>
    <img src="{{ url_for('static', filename='python-logo.png') }}" />
  </body>
</html>
