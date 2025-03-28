<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">AI-README.GIT</h1></p>
<p align="center">
	<em>Orchestrating AI to Streamline Your Search Experience</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Maurin2/Ai-README.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Maurin2/Ai-README.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Maurin2/Ai-README.git?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Maurin2/Ai-README.git?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The Ai-README.git project revolutionizes real-time data retrieval and processing by seamlessly integrating AI-driven search capabilities with user interactions. This innovative platform features a robust architecture that supports dynamic information fetching, caching, and intelligent response generation, making it ideal for developers and businesses seeking to enhance their applications with efficient and contextually relevant search functionalities.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a multi-service architecture with components for orchestration, frontend, and scraping.</li><li>Employs `<Docker>` for containerization, enhancing portability and consistency across environments.</li><li>Uses `<FastAPI>` and `<Streamlit>` frameworks for backend and frontend services, respectively.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Adheres to modern Python practices with structured project directories and separation of concerns.</li><li>Includes detailed configuration files like `nginx.conf` and `logging.conf` for custom setups.</li><li>Source code is modular, facilitating easy maintenance and scalability.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation with usage of `<pip>` and `<Docker>` for setup and deployment.</li><li>Rich in comments within configuration files and scripts to aid understanding and usage.</li><li>Documentation includes examples and commands for building and running services.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with external APIs and services using `<Python>` libraries for HTTP requests and data handling.</li><li>Supports `<Redis>` for caching, enhancing performance by reducing data retrieval times.</li><li>Utilizes `<Playwright>` and `<aiohttp>` for robust web scraping capabilities.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Project is divided into multiple sub-modules like orchestrator, frontend, and scraper, each with its own Dockerfile and requirements.</li><li>Codebase supports plug-and-play functionality for easy replacement or upgrading of individual components.</li><li>Each module can be developed, tested, and deployed independently.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes setup for testing with `<pytest>`, ensuring reliability and robustness of the application.</li><li>Mock data and testing scripts like `test_dict.py` are used to simulate external interactions.</li><li>Testing commands and configurations are well-documented for ease of use.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Leverages asynchronous programming models in Python to enhance I/O operations.</li><li>Uses `<Redis>` for efficient data caching and retrieval, significantly improving response times.</li><li>Optimized Docker configurations ensure minimal overhead in containerized environments.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements security best practices in Docker configurations and NGINX setups.</li><li>Uses environment variables and `.env.example` for secure management of credentials and configuration settings.</li><li>APIs are designed to handle errors gracefully, preventing common security issues like injections.</li></ul> |

---

## 📁 Project Structure

```sh
└── Ai-README.git/
    ├── Solucion a la tarea
    │   ├── Arquitectura_de_Chatbot.png.png
    │   ├── Diagrama_de_Clases.png.png
    │   ├── Interaccion_del_Chatbot.png.png
    │   ├── Proceso_de_Recuperacion.png.png
    │   └── solucion copy.md
    ├── challenge.md
    ├── project
    │   ├── .env.example
    │   ├── .gitignore
    │   ├── LICENSE
    │   ├── docker-compose.yml
    │   ├── pyproject.toml
    │   ├── redis_data
    │   ├── src
    │   └── tests
    └── solucion.md
```


### 📂 Project Index
<details open>
	<summary><b><code>AI-README.GIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			</table>
		</blockquote>
	</details>
	<details> <!-- project Submodule -->
		<summary><b>project</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/pyproject.toml'>pyproject.toml</a></b></td>
				<td>- Defines the configuration for the "me-com" project using Poetry, specifying project metadata including the name, version, and author details<br>- It sets Python 3.11 as a dependency and outlines the package structure to include the "me" directory<br>- Additionally, it configures the build system with requirements for Poetry, ensuring a streamlined package management and distribution process.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/.env.example'>.env.example</a></b></td>
				<td>- Establishes default configuration settings for network requests and API interactions within the software architecture<br>- It specifies headers for HTTP requests and provides placeholders for essential API credentials, ensuring streamlined access to Google's Custom Search API and OpenAI services, crucial for the application's data retrieval and processing functionalities.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/docker-compose.yml'>docker-compose.yml</a></b></td>
				<td>- Defines the architecture for a multi-service application, orchestrating interactions between a web frontend, an API backend, and a caching service<br>- The configuration sets up an API server using Uvicorn, a frontend using Streamlit, and a Redis database for caching, ensuring smooth communication and data management across services.</td>
			</tr>
			</table>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<details>
						<summary><b>orchestrator</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/main.py'>main.py</a></b></td>
								<td>- Orchestrates real-time information retrieval and response generation by integrating various components such as caching, scraping, and AI-driven text embeddings<br>- It leverages a FastAPI framework to stream search results and interactive chat responses, enhancing user queries with contextually relevant data.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/requirements.txt'>requirements.txt</a></b></td>
								<td>- Defines the specific Python packages and their versions required for the orchestrator component of the project, ensuring compatibility and functionality across the services<br>- It includes libraries for asynchronous operations, web frameworks, data handling, and machine learning, crucial for the component's operation within the broader system architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/logging.conf'>logging.conf</a></b></td>
								<td>- Configures logging for the project, setting up different loggers, handlers, and formatters to manage output verbosity and format<br>- It distinguishes between general and detailed logging, directing the latter to a specific application component, uicheckapp, enhancing debug capabilities and traceability without cluttering the primary log stream.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/Dockerfile'>Dockerfile</a></b></td>
								<td>- Sets up a Docker container for a Python-based web application, installing necessary dependencies and a language model<br>- It prepares the environment to run a FastAPI application using Uvicorn as the server, configured to reload on changes and listen on all network interfaces at port 8000.</td>
							</tr>
							</table>
							<details>
								<summary><b>mocks</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/mocks/test_dict.py'>test_dict.py</a></b></td>
										<td>- Provides a mock dictionary of search results related to the LangChain framework, simulating responses for testing the functionality of components that process and display search data within the application<br>- This aids in ensuring the robustness and accuracy of features that interact with external search results in the development environment.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/models/document.py'>document.py</a></b></td>
										<td>- Defines a `Document` model using Pydantic, essential for managing document data within the orchestrator module<br>- It includes attributes for text content, URL, vector representation, and similarity score, facilitating operations like document comparison and retrieval across the system's architecture, enhancing data handling and processing efficiency.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/models/search.py'>search.py</a></b></td>
										<td>- Defines data models for handling search results within the orchestrator component of the system<br>- Models include structures for thumbnails, page metadata, and detailed search documents, facilitating the organization and retrieval of search data such as links, titles, snippets, and visual previews from various sources.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>retrieval</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/retrieval/retriever.py'>retriever.py</a></b></td>
										<td>- Retriever orchestrates the retrieval of relevant documents based on user queries, leveraging cached data and online sources<br>- It utilizes embeddings for semantic analysis and cosine similarity to ensure relevance<br>- The process includes fetching, splitting, and embedding text data, enhancing efficiency and accuracy in information retrieval within the system.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/retrieval/scraper.py'>scraper.py</a></b></td>
										<td>- Scraper.py defines abstract and concrete classes for web scraping, facilitating both local and remote text retrieval from URLs<br>- It abstracts fetching and parsing HTML content, returning structured text data<br>- The architecture supports scalability and integration within a larger system, handling asynchronous web requests efficiently.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/retrieval/cache.py'>cache.py</a></b></td>
										<td>- Manages the storage and retrieval of document vectors in a Redis database, enabling efficient similarity searches and caching mechanisms<br>- It includes functionalities for initializing the database, inserting new documents only if they are sufficiently unique, and finding documents similar to a given vector.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/retrieval/splitter.py'>splitter.py</a></b></td>
										<td>- Splitter.py defines abstract and concrete classes for text segmentation, crucial for handling large texts by breaking them into manageable chunks<br>- It includes a generic splitter interface and specific implementations using recursive character-based methods and semantic clustering with Spacy, enhancing text processing capabilities within the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/retrieval/embeddings.py'>embeddings.py</a></b></td>
										<td>- Embeddings.py defines an abstract base class for embedding services, ensuring a standardized approach for converting text chunks into numerical vectors<br>- It includes implementations for both a remote service and OpenAI's API, each returning embeddings with specified vector dimensions, facilitating seamless integration into the broader system for natural language processing tasks.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/retrieval/search.py'>search.py</a></b></td>
										<td>- Searcher classes within the `project/src/orchestrator/retrieval/search.py` facilitate querying external search engines, specifically Google, using API calls<br>- They handle the construction and execution of search queries, manage API interactions, and parse responses into structured search results, ensuring robust error handling and fallback mechanisms.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>prompt</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/prompt/prompt.py'>prompt.py</a></b></td>
										<td>- Serves as a template generator within the orchestrator module, crafting structured prompts for user queries<br>- It formats user input into a predefined template, ensuring responses are informative and clear<br>- This component is crucial for maintaining consistency in user interactions across the system, enhancing the clarity and reliability of information exchange within the application's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>util</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/orchestrator/util/logger.py'>logger.py</a></b></td>
										<td>- Establishes the logging configuration for the project, setting a debug level and a specific format for messages<br>- It configures a console handler to output log messages to standard error<br>- This setup aids in monitoring and debugging by providing real-time logging information, crucial for maintaining the operational health of the application.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>frontend</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/frontend/main.py'>main.py</a></b></td>
								<td>- Manages the user interface for a chat-based application, handling user inputs, displaying chat history, and processing responses from a backend service<br>- It utilizes streaming data to dynamically update the chat interface and includes functionality for rendering interactive elements based on backend data.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/frontend/requirements.txt'>requirements.txt</a></b></td>
								<td>- Specifies the dependencies required for the frontend component of the application, ensuring compatibility and functionality within the user interface<br>- It includes libraries for HTTP communication, server-sent events handling, and the Streamlit framework, which facilitates the creation of interactive web applications directly from Python scripts, enhancing the project's interactivity and user engagement.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/frontend/Dockerfile'>Dockerfile</a></b></td>
								<td>- Sets up a Docker container for the frontend component of the application, using Python 3.11<br>- It establishes a working directory, installs dependencies from a requirements file, and copies the main application file<br>- The container is configured to run a Streamlit application on port 80, accessible from any network interface.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>scraper</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/scraper/nginx.conf'>nginx.conf</a></b></td>
								<td>- Configures an NGINX server to manage network connections and route traffic within the scraper service<br>- It sets up a proxy to distribute incoming requests to the app_servers, enhancing load handling by allowing 1024 worker connections<br>- The configuration ensures efficient request forwarding and client IP address retention for the application's operational needs.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/scraper/main.py'>main.py</a></b></td>
								<td>- Main.py serves as the core component of a web scraping service within the project, utilizing FastAPI to expose an endpoint that asynchronously scrapes HTML content from specified URLs<br>- It leverages Playwright for browser-based scraping and aiohttp for HTTP requests, handling potential timeouts and providing the scraped data through a RESTful API.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/scraper/requirements.txt'>requirements.txt</a></b></td>
								<td>- Defines the dependencies required for the scraper module within the broader project architecture, ensuring compatibility and functionality<br>- It includes libraries for asynchronous operations, web scraping, server handling, and data validation, pivotal for the scraper's performance in data extraction and API interactions within the project's ecosystem.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/src/scraper/Dockerfile'>Dockerfile</a></b></td>
								<td>- Establishes the environment for a Python-based web scraping application, setting up a Docker container with necessary dependencies<br>- It installs Python packages, Playwright for browser automation, and configures the server to run the application on Uvicorn, making it ready for deployment and scalable web scraping operations within the project's architecture.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>redis_data</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Maurin2/Ai-README.git/blob/master/project/redis_data/dump.rdb'>dump.rdb</a></b></td>
						<td>- Manages the persistence layer for the application's Redis database, specifically handling data serialization and storage<br>- It ensures efficient data retrieval and storage by organizing data into structured formats like text, URLs, vectors, and JSON, optimizing memory usage and access speeds within the broader system architecture.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Ai-README.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


### ⚙️ Installation

Install Ai-README.git using one of the following methods:

**Build from source:**

1. Clone the Ai-README.git repository:
```sh
❯ git clone https://github.com/Maurin2/Ai-README.git
```

2. Navigate to the project directory:
```sh
❯ cd Ai-README.git
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r project/src/orchestrator/requirements.txt, project/src/frontend/requirements.txt, project/src/scraper/requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t Maurin2/Ai-README.git .
```




### 🤖 Usage
Run Ai-README.git using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/Maurin2/Ai-README.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Maurin2/Ai-README.git/issues)**: Submit bugs found or log feature requests for the `Ai-README.git` project.
- **💡 [Submit Pull Requests](https://github.com/Maurin2/Ai-README.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Maurin2/Ai-README.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Maurin2/Ai-README.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Maurin2/Ai-README.git">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
