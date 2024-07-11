## Flask Application Design

### HTML Files

- **index.html:**
   - Main page of the application.
   - Displays a table with the cheapest flight prices to each destination.
   - Includes a form to allow users to refresh the prices.

### Routes

- **@app.route('/')**
   - Maps to the 'index.html' file.
   - Displays the main page.

- **@app.route('/refresh', methods=['POST'])**
   - Refreshes the flight prices and updates the table on the main page.
   - Makes an API call to a service that provides flight prices.
   - Filters out results from "Spring Airlines" using the API's filtering capabilities.

- **@app.route('/about')**
   - Maps to an 'about.html' file.
   - Displays information about the application, its purpose, and usage instructions.

### Implementation Notes

- Utilize Flask's built-in templating engine (Jinja2) in the HTML files to dynamically display the flight prices.
- Use Bootstrap's CSS framework for the front-end design and styling.
- Consider using an external API or service for retrieving flight prices.
- Implement error handling to gracefully handle any API errors or unexpected conditions.