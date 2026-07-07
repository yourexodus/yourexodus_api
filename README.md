# 🏪 Flask Store API

A fully functional **RESTful API** built with **Flask-Smorest** to manage store inventory, including items, stores, tags, and users.
This project demonstrates best practices in API design, modular architecture, and Docker-based deployment — built while balancing full-time work and motherhood 💪🏽.

---

## 🚀 Features

- 🔹 CRUD operations for **Users**, **Stores**, **Items**, and **Tags**
- 🔹 RESTful routing with parameterized endpoints
- 🔹 Input validation and robust error handling (404, 400)
- 🔹 Modular architecture using **Blueprints** and **MethodViews**
- 🔹 Auto-generated API documentation with **Swagger UI**
- 🔹  
- 🔹 Dockerized for scalable deployment

---

## 🛠️ Tech Stack

| Category | Tools |
|-----------|--------|
| **Language** | Python |
| **Framework** | Flask, Flask-Smorest |
| **Auth & Security** | Flask-JWT-Extended |
| **Testing / Docs** | Insomnia, Swagger UI |
| **Deployment** | Docker |
| **Version Control** | Git & GitHub |

---
## 🧩 Project Structure

<table>
<thead>
<tr>
<th>Linked Code Breakdown</th>
<th>File Structure Layout</th>
</tr>
</thead>
<tbody>
<tr>
<td>
This outlines the organization of the API, with links to the core components.
</td>
<td rowspan="8">
<pre>
mfrancis_restAPI/
├── .venv/
├── blocklist.py
├── app.py
├── db.py
├── schemas.py
├── Dockerfile
├── requirements.txt
├── models/
│   ├── store.py
│   ├── item.py
│   └── user.py
└── resources/
    ├── store.py
    ├── item.py
    ├── user.py
    └── tag.py
</pre>
</td>
</tr>
<tr>
<td>
<a href="https://github.com/yourexodus/mfrancis_restAPI/tree/main/models"><code>/models</code></a><br>
<em>SQLAlchemy database models (Store, Item, User).</em>
</td>
</tr>
<tr>
<td>
<a href="https://github.com/yourexodus/mfrancis_restAPI/tree/main/resources"><code>/resources</code></a><br>
<em>API Blueprints/MethodViews (User, Store, Item, Tag).</em>
</td>
</tr>
<tr>
<td>
<a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/app.py"><code>app.py</code></a><br>
<em>Flask application entry point.</em>
</td>
</tr>
<tr>
<td>
<a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/db.py"><code>db.py</code></a><br>
<em>Database initialization (SQLAlchemy instance).</em>
</td>
</tr>
<tr>
<td>
<a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/blocklist.py"><code>blocklist.py</code></a><br>
<em>JWT token blocklist for logout/revocation.</em>
</td>
</tr>
<tr>
<td>
<a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/schemas.py"><code>schemas.py</code></a><br>
<em>Marshmallow schemas for request/response validation.</em>
</td>
</tr>
<tr>
<td>
<a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/requirements.txt"><code>requirements.txt</code></a><br>
<em>Project dependencies list.</em>
</td>
</tr>
</tbody>
</table>

---
## 🏬 Store Management Flow (CRUD Operations)

<table>
<thead>
<tr>
<th>Linked Code Breakdown</th>
<th>Flowchart Diagram</th>
</tr>
</thead>
<tbody>
<tr>
<td>
This section outlines the essential CRUD operations for the Store resource, with links to the relevant code in <code>resources/store.py</code>.
</td>
<td rowspan="6">
<img src="https://github.com/yourexodus/MarlainnaTheAnalyst/blob/main/RestApi/images/store_chart.png" alt="Simplified Store Flowchart: Create, View All, View by ID, Update, Delete" width="100%"/>
</td>
</tr>
<tr>
<td>
<strong>1. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/store.py#L18">Create Store</a></strong><br>
<em>Creates a new store entry in the database.</em>
</td>
</tr>
<tr>
<td>
<strong>2. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/store.py#L38">View All Stores</a></strong><br>
<em>Retrieves a list of all available stores.</em>
</td>
</tr>
<tr>
<td>
<strong>3. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/store.py#L32">View Store by ID</a></strong><br>
<em>Retrieves details for a specific store.</em>
</td>
</tr>
<tr>
<td>
<strong>4. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/store.py#L25">Update Store</a></strong><br>
<em>Modifies the details of an existing store.</em>
</td>
</tr>
<tr>
<td>
<strong>5. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/store.py#L42">Delete Store</a></strong><br>
<em>Permanently removes a store from the database.</em>
</td>
</tr>
</tbody>
</table>
> This section summarizes the complete Store Management Process, detailing how stores are created, viewed, modified, and removed.

---
## 🏷️ Tag Management Flow (CRUD Operations)

<table>
<thead>
<tr>
<th>Linked Code Breakdown</th>
<th>Flowchart Diagram</th>
</tr>
</thead>
<tbody>
<tr>
<td>
This section outlines the essential CRUD operations for the Tag resource, with links to the relevant code in <code>resources/tag.py</code>.
</td>
<td rowspan="6">
<img src="https://github.com/yourexodus/MarlainnaTheAnalyst/blob/main/RestApi/images/tag_chart.png" alt="Simplified Tag Flowchart: Create, View All, View by ID, Update, Delete" width="100%"/>
</td>
</tr>
<tr>
<td>
<strong>1. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/tag.py#L18">Create Tag</a></strong><br>
<em>Creates a new tag entry and links it to an item or store.</em>
</td>
</tr>
<tr>
<td>
<strong>2. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/tag.py#L38">View All Tags</a></strong><br>
<em>Retrieves a list of all available tags.</em>
</td>
</tr>
<tr>
<td>
<strong>3. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/tag.py#L32">View Tag by ID</a></strong><br>
<em>Retrieves details for a specific tag.</em>
</td>
</tr>
<tr>
<td>
<strong>4. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/tag.py#L25">Update Tag</a></strong><br>
<em>Modifies the name or details of an existing tag.</em>
</td>
</tr>
<tr>
<td>
<strong>5. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/tag.py#L42">Delete Tag</a></strong><br>
<em>Permanently removes a tag from the database.</em>
</td>
</tr>
</tbody>
</table>

> This visualization details the complete Tag Management Process, including tag creation, retrieval, and deletion.

---
## 📦 Item Management Flow (CRUD Operations)

<table>
<thead>
<tr>
<th>Linked Code Breakdown</th>
<th>Flowchart Diagram</th>
</tr>
</thead>
<tbody>
<tr>
<td>
This section outlines the essential CRUD operations for the Item resource, with links to the relevant code in <code>resources/item.py</code>.
</td>
<td rowspan="6">
<img src="https://github.com/yourexodus/MarlainnaTheAnalyst/blob/main/RestApi/images/item_chart.png" alt="Simplified Item Flowchart: Create, View All, View by ID, Update, Delete" width="100%"/>
</td>
</tr>
<tr>
<td>
<strong>1. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/item.py#L18">Create Item</a></strong><br>
<em>Adds a new item, typically linked to a specific store.</em>
</td>
</tr>
<tr>
<td>
<strong>2. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/item.py#L38">View All Items</a></strong><br>
<em>Retrieves a comprehensive list of all items across all stores.</em>
</td>
</tr>
<tr>
<td>
<strong>3. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/item.py#L32">View Item by ID</a></strong><br>
<em>Retrieves details for a specific item.</em>
</td>
</tr>
<tr>
<td>
<strong>4. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/item.py#L25">Update Item</a></strong><br>
<em>Modifies the details (e.g., price, name) of an existing item.</em>
</td>
</tr>
<tr>
<td>
<strong>5. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/item.py#L42">Delete Item</a></strong><br>
<em>Permanently removes an item from the database.</em>
</td>
</tr>
</tbody>
</table>

> This visualization details the complete Item Management Process, including item creation, retrieval, and deletion.

---
## ✅ User Flow (Authentication & Authorization)

<table>
<thead>
<tr>
<th>Linked Code Breakdown</th>
<th>Flowchart Diagram</th>
</tr>
</thead>
<tbody>
<tr>
<td>
This outlines the key steps in the user authentication and authorization process, with links to the relevant code in your <code>mfrancis_restAPI</code> repository.
</td>
<td rowspan="7">
<img src="https://github.com/yourexodus/MarlainnaTheAnalyst/blob/main/RestApi/images/UserFlowchart.png" alt="User Authentication Flowchart" width="100%"/>
</td>
</tr>
<tr>
<td>
<strong>1. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/user.py">User Registration</a></strong><br>
<em>This step handles new user account creation.</em>
</td>
</tr>
<tr>
<td>
<strong>2. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/user.py#L36">Valid Credentials Check</a></strong><br>
<em>Verifies the provided username and password during login.</em>
</td>
</tr>
<tr>
<td>
<strong>3. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/user.py#L42">Generate JWT (JSON Web Token)</a></strong><br>
<em>Upon successful credential validation, a JWT is created for the user session.</em>
</td>
</tr>
<tr>
<td>
<strong>4. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/resources/user.py#L35">Login</a></strong><br>
<em>The process where an existing user authenticates with their credentials.</em>
</td>
</tr>
<tr>
<td>
<strong>5. <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/app.py#L41">Valid JWT Check</a></strong><br>
<em>Ensures the JWT provided with subsequent requests is valid and not expired or blacklisted.</em>
</td>
</tr>
<tr>
<td>
(See also: <a href="https://github.com/yourexodus/mfrancis_restAPI/blob/main/blocklist.py">JWT Blocklist</a>)
</td>
</tr>
</tbody>
</table>

> This flowchart illustrates the **User Authentication Process**, including registration, login, token creation, and JWT validation.

---
<!-- API Testing (with Insomnia) - paste this under your "User" section -->
<section id="api-testing" style="margin-top:1.5rem;">
  <h2 style="font-size:1.25rem; margin-bottom:0.25rem;">🧪 API Testing (with Insomnia)</h2>
  <p style="margin-top:0; margin-bottom:0.75rem;">
    I verified all REST API endpoints using <strong>Insomnia</strong>, <code>pytest</code>, and manual checks to ensure reliability,
    authentication, and proper error handling.
  </p>

  <!-- Badge -->
  <p style="margin:0 0 0.75rem 0;">
    <img alt="Tested with Insomnia" src="https://img.shields.io/badge/Tested%20With-Insomnia-purple?logo=insomnia" style="vertical-align:middle;">
    &nbsp;
    <a href="https://docs.google.com/document/d/e/2PACX-1vT70eScmMd-kH5hozehk0BMeGaVpRpAYFy9JCqHy0oQoAd_04LikDVhA8BFOWSIFm2yvtG_teVL7oiY/pub" target="_blank" rel="noopener noreferrer">
      View full testing report (screenshots & steps)
    </a>
  </p>

  <!-- Table -->
  <div style="overflow-x:auto;">
    <table style="width:100%; border-collapse:collapse; font-family:system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;">
      <thead>
        <tr>
          <th style="text-align:left; padding:8px 12px; border-bottom:2px solid #e1e4e8;">Test Type</th>
          <th style="text-align:left; padding:8px 12px; border-bottom:2px solid #e1e4e8;">Tool / Method</th>
          <th style="text-align:left; padding:8px 12px; border-bottom:2px solid #e1e4e8;">Purpose</th>
          <th style="text-align:left; padding:8px 12px; border-bottom:2px solid #e1e4e8;">Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Manual Testing</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;"><code>Flask</code> test server</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Verified CRUD operations and JSON responses</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;"><code>/item</code>, <code>/store</code>, <code>/user/register</code></td>
        </tr>
        <tr>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Token Verification</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;"><a href="https://jwt.io/" target="_blank" rel="noopener noreferrer">jwt.io</a></td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Validated JWT access tokens & signature</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Signature ✅ verified</td>
        </tr>
        <tr>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Automated Tests</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;"><code>pytest</code> + <code>Flask test_client()</code></td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Endpoint logic, response codes, error handling</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;"><code>test_create_item()</code>, <code>test_login_user()</code></td>
        </tr>
        <tr>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">API Client Testing</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;"><strong>Insomnia</strong></td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Sent authenticated requests with JWT headers; tested JSON payloads</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">GET <code>/item/1</code>, POST <code>/store</code></td>
        </tr>
        <tr>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Error Handling</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Manual & mock inputs</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">Confirmed messages for expired/invalid/missing tokens</td>
          <td style="padding:10px 12px; border-bottom:1px solid #f1f1f1;">`401 token_expired`, `401 invalid_token`</td>
        </tr>
        <tr>
          <td style="padding:10px 12px;">Database Validation</td>
          <td style="padding:10px 12px;"><code>SQLite Browser</code> / SQLAlchemy logs</td>
          <td style="padding:10px 12px;">Ensured persistent storage after CRUD operations</td>
          <td style="padding:10px 12px;">Checked <code>data.db</code> for correct table updates</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
--
## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone [https://github.com/yourexodus/mfrancis_restAPI.git](https://github.com/yourexodus/mfrancis_restAPI.git)
cd mfrancis_restAPI
2. Create a Virtual Environment
Bash

python -m venv .venv
source .venv/Scripts/activate    # (Windows)
# source .venv/bin/activate     # (macOS/Linux)
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Run the Flask API
Bash

flask run
👉 http://127.0.0.1:5000/swagger-ui to view the automatically generated Swagger documentation.

5. Docker Usage
Bash

docker build -t flask-store-api .
docker run -p 5000:5000 flask-store-api
