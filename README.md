<!-- Ref Material -->
<!-- Flask -->

https://flask.palletsprojects.com/en/2.0.x/

<!-- Youtube vid -->

https://www.youtube.com/watch?v=Qr4QMBUPxWo

<!-- GitHub -->

https://github.com/jimdevops19/FlaskSeries

<!-- Help with the server operation -->

https://flask.palletsprojects.com/en/2.0.x/cli/

<!-- HardCode way of username info -->

# THis is the hard coded way of doing a username input- this is not dyanmic

# @app.route('/about/<username>')

# def about_page(username):

# return f'<h1>THis is the about page of {username}</h1>'

<!-- Ref- market.html ln69 -->

{% for item in items %}

<!-- The for loop allows for the iteration over the list and dynamically builds the table based on the number of items in the list. -->
<tr>
<td>{{ item.id }}</td>
<td>{{ item. name }}</td>
<td>{{ item.barcode }}</td>
<td>$ {{ item.price }}</td>
</tr>
{% endfor %}
</tbody>

<!-- Old Home page html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x"
      crossorigin="anonymous"
    />
    <title>Home Page</title>
  </head>
  <!-- NavBar -->
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#"
              >Home <span class="sr-only">(current)</span></a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
  <!-- Body -->
  <body>
    <main>
      <h1>Welcome to the home page</h1>
      <!-- Footer -->
      <footer></footer>
    </main>
    <!-- Script links -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
      crossorigin="anonymous"
    ></script>
  </body>
  <style>
    body {
      background-color: #212121;
      color: white;
    }
  </style>
</html>

<!-- The old Market html  -->
<!-- Kept for the table -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x"
      crossorigin="anonymous"
    />
    <title>Market Page</title>
  </head>
  <!-- NavBar -->
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#"
              >Home <span class="sr-only">(current)</span></a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
  <!-- Body -->
  <body>
    <main>
      <h1>Welcome to the Market page</h1>
      <!-- Table -->
      <table class="table table-hover table-dark">
        <thead>
          <tr>
            <!-- Your Columns HERE -->
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Barcode</th>
            <th scope="col">Price</th>
            <th scope="col">Options</th>
          </tr>
        </thead>
        <tbody>
          <!-- Your rows inside the table HERE: -->
          {% for item in items %}
          <tr>
            <td>{{ item.id }}</td>
            <td>{{ item. name }}</td>
            <td>{{ item.barcode }}</td>
            <td>$ {{ item.price }}</td>
            <td>
              <button class="btn btn-outline btn-info">More Info</button>
              <button class="btn btn-outline btn-success">
                Purchase this item
              </button>
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
      <!-- Footer -->
      <footer></footer>
    </main>
    <!-- Script links -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
      crossorigin="anonymous"
    ></script>
  </body>
  <style>
    body {
      background-color: #212121;
      color: white;
    }
  </style>
</html>
