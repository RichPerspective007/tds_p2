from sentence_transformers import SentenceTransformer
# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
import requests

ga1questions = [
    "Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of code -s?",
    "Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL. Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 22f3000819@ds.study.iitm.ac.in What is the JSON output of the command? (Paste only the JSON body, not the headers)",
    "Let's make sure you know how to use npx and prettier. Download README.md. In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md | sha256sum. What is the output of the command?",
    "Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel) `=SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 5, 2), 1, 10))` What is the result?",
    "Let's make sure you can write formulas in Excel. Type this formula into Excel. Note: This will ONLY work in Office 365. `=SUM(TAKE(SORTBY({13,11,0,9,5,0,15,2,12,15,5,0,2,0,14,9}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 9))` What is the result? Note: If you get #NAME? you have the wrong version of Excel. Find a friend for whom this works.",
    "Just above this paragraph, there's a hidden input with a secret value. What is the value in the hidden input?",
    "How many Wednesdays are there in the date range 1987-06-21 to 2009-03-20?",
    "Download and unzip file q-extract-csv-zip.zip which has a single extract.csv file inside. What is the value in the \"answer\" column of the CSV file?",
    "Let's make sure you know how to use JSON. Sort this JSON array of objects by the value of the age field. In case of a tie, sort by the name field. Paste the resulting JSON below without any spaces or newlines. `[{\"name\":\"Alice\",\"age\":3},{\"name\":\"Bob\",\"age\":14},{\"name\":\"Charlie\",\"age\":94},{\"name\":\"David\",\"age\":67},{\"name\":\"Emma\",\"age\":64},{\"name\":\"Frank\",\"age\":60},{\"name\":\"Grace\",\"age\":70},{\"name\":\"Henry\",\"age\":99},{\"name\":\"Ivy\",\"age\":2},{\"name\":\"Jack\",\"age\":86},{\"name\":\"Karen\",\"age\":96},{\"name\":\"Liam\",\"age\":22},{\"name\":\"Mary\",\"age\":10},{\"name\":\"Nora\",\"age\":48},{\"name\":\"Oscar\",\"age\":28},{\"name\":\"Paul\",\"age\":22}]` Sorted JSON:",
    "Download q-multi-cursor-json.txt  and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}. What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?",
    "Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value attributes? Sum of data-value attributes:",
    "Download and process the files in q-unicode-data.zip which contains three files with different encodings: data1.csv: CSV file encoded in CP-1252 data2.csv: CSV file encoded in UTF-8 data3.txt: Tab-separated file encoded in UTF-16 Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches › OR Œ OR … across all three files. What is the sum of all values associated with these symbols?",
    "Let's make sure you know how to use GitHub. Create a GitHub account if you don't have one. Create a new public repository. Commit a single JSON file called email.json with the value {\"email\": \"22f3000819@ds.study.iitm.ac.in\"} and push it. Enter the raw Github URL of email.json so we can verify it. (It might look like https://raw.githubusercontent.com/[GITHUB ID]/[REPO NAME]/main/email.json.)",
    "Download q-replace-across-files.zip and unzip it into a new folder, then replace all \"IITM\" (in upper, lower, or mixed case) with \"IIT Madras\" in all files. Leave everything as-is - don't change the line endings. What does running cat * | sha256sum in that folder show in bash?",
    "Download q-list-file-attributes.zip and extract it. Use ls with options to list all files in the folder along with their date and file size. What's the total size of all files at least 1018 bytes large and modified on or after Wed, 10 Dec, 2008, 1:37 am IST? Don't copy from inside the ZIP file or use Windows Explorer to unzip. That destroys the timestamps. Extract using unzip, 7-Zip or similar utilities and check the timestamps.",
    "Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt. What does running grep . * | LC_ALL=C sort | sha256sum in bash on that folder show?",
    "Download q-compare-files.zip and extract it. It has 2 nearly identical files, a.txt and b.txt, with the same number of lines. How many lines are different between a.txt and b.txt?",
    "There is a tickets table in a SQLite database that has columns type, units, and price. Each row is a customer bid for a concert ticket.type	units	price BRONZE	408	1.44 Gold	327	1.8 BRONZE	962	1.46 Gold	185	0.77 gold	88	1.5 ... What is the total sales of all the items in the \"Gold\" ticket type? Write SQL to calculate it. Get all rows where the Type is \"Gold\". Ignore spaces and treat mis-spellings like GOLD, gold, etc. as \"Gold\". Calculate the sales as Units * Price, and sum them up.",
]

ga2questions = [
    "Write documentation in Markdown for an *imaginary* analysis of the number of steps you walked each day for a week, comparing over time and with friends. The Markdown must include: Top-Level Heading: At least 1 heading at level 1, e.g., # Introduction Subheadings: At least 1 heading at level 2, e.g., ## Methodology Bold Text: At least 1 instance of bold text, e.g., *important* Italic Text: At least 1 instance of italic text, e.g., note Inline Code: At least 1 instance of inline code, e.g., sample_code Code Block: At least 1 instance of a fenced code block, e.g. print(\"Hello World\") Bulleted List: At least 1 instance of a bulleted list, e.g., - Item Numbered List: At least 1 instance of a numbered list, e.g., 1. Step One Table: At least 1 instance of a table, e.g., | Column A | Column B | Hyperlink: At least 1 instance of a hyperlink, e.g., [Text](https://example.com) Image: At least 1 instance of an image, e.g., ![Alt Text](https://example.com/image.jpg) Blockquote: At least 1 instance of a blockquote, e.g., > This is a quote Enter your Markdown here:",
    "Download the image below and compress it losslessly to an image that is less than 1,500 bytes. By losslessly, we mean that every pixel in the new image should be identical to the original image. Upload your losslessly compressed image (less than 1,500 bytes)",
    "Publish a page using GitHub Pages that showcases your work. Ensure that your email address 22f3000819@ds.study.iitm.ac.in is in the page's HTML. GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a: <!--email_off-->22f3000819@ds.study.iitm.ac.in<!--/email_off--> What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/ If a recent change that's not reflected, add ?v=1, ?v=2 to the URL to bust the cache.",
    "Let's make sure you can access Google Colab. Run this program on Google Colab, allowing all required access to your email ID: 22f3000819@ds.study.iitm.ac.in. import hashlib import requests from google.colab import auth from oauth2client.client import GoogleCredentials auth.authenticate_user() creds = GoogleCredentials.get_application_default() token = creds.get_access_token().access_token response = requests.get(\"https://www.googleapis.com/oauth2/v1/userinfo\", params={\"alt\": \"json\"}, headers={\"Authorization\": f\"Bearer {token}\"}) email = response.json()[\"email\"] hashlib.sha256(f\"{email} {creds.token_expiry.year}\".encode()).hexdigest()[-5:] What is the result? (It should be a 5-character string)",
    "Download this image. Create a new Google Colab notebook and run this code (after fixing a mistake in it) to calculate the number of pixels with a certain minimum brightness:import numpy as np from PIL import Image from google.colab import files import colorsys # There is a mistake in the line below. Fix it image = Image.open(list(files.upload().keys)[0]) rgb = np.array(image) / 255.0 lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb) light_pixels = np.sum(lightness > 0.163) print(f'Number of pixels with lightness > 0.163: {light_pixels}')``` What is the result? (It should be a number)",
    "Download this  which has the marks of 100 imaginary students. Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON response with the marks of the names X and Y in the same order, like this: { \"marks\": [10, 20] } Make sure you enable CORS to allow GET requests from any origin. What is the Vercel URL? It should look like: https://your-app.vercel.app/api",
    """Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address 22f3000819@ds.study.iitm.ac.in. For example:
        jobs:
        test:
            steps:
            - name: 22f3000819@ds.study.iitm.ac.in
                run: echo "Hello, world!"
            
        Trigger the action and make sure it is the most recent action.

        What is your repository URL? It will look like: https://github.com/USER/REPO""",
    "Create and push an image to Docker Hub. Add a tag named 22f3000819 to the image. What is the Docker image URL? It should look like: https://hub.docker.com/repository/docker/$USER/$REPO/general",
    """Download . This file has 2-columns:
        studentId: A unique identifier for each student, e.g. 1, 2, 3, ...
        class: The class (including section) of the student, e.g. 1A, 1B, ... 12A, 12B, ... 12Z
        Write a FastAPI server that serves this data. For example, /api should return all students data (in the same row and column order as the CSV file) as a JSON like this:
        {
        "students": [
            {
            "studentId": 1,
            "class": "1A"
            },
            {
            "studentId": 2,
            "class": "1B"
            }, ...
        ]
        }
        If the URL has a query parameter class, it should return only students in those classes. For example, /api?class=1A should return only students in class 1A. /api?class=1A&class=1B should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).
        Make sure you enable CORS to allow GET requests from any origin.
        What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
        We'll check by sending a request to this URL with ?class=... added and check if the response matches the data.""",
    "Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6_K.llamafile model with it. Create a tunnel to the Llamafile server using ngrok. What is the ngrok URL? It might look like: https://[random].ngrok-free.app/",
]

ga3questions = [
    """DataSentinel Inc. is a tech company specializing in building advanced natural language processing (NLP) solutions. Their latest project involves integrating an AI-powered sentiment analysis module into an internal monitoring dashboard. The goal is to automatically classify large volumes of unstructured feedback and text data from various sources as either GOOD, BAD, or NEUTRAL. As part of the quality assurance process, the development team needs to test the integration with a series of sample inputs—even ones that may not represent coherent text—to ensure that the system routes and processes the data correctly.

    Before rolling out the live system, the team creates a test harness using Python. The harness employs the httpx library to send POST requests to OpenAI's API. For this proof-of-concept, the team uses the dummy model gpt-4o-mini along with a dummy API key in the Authorization header to simulate real API calls.

    One of the test cases involves sending a sample piece of meaningless text:

    gfP  B 7ksf   u Q8AbVynO P TdJ zWDt glcAZ0GO r2B1b
    Write a Python program that uses httpx to send a POST request to OpenAI's API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:

    Make sure you pass an Authorization header with dummy API key.
    Use gpt-4o-mini as the model.
    The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.
    The second message must be exactly the text contained above.
    This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications.

    Note: This uses a dummy httpx library, not the real one. You can only use:

    response = httpx.get(url, **kwargs)
    response = httpx.post(url, json=None, **kwargs)
    response.raise_for_status()
    response.json()
    Code""",
    """LexiSolve Inc. is a startup that delivers a conversational AI platform to enterprise clients. The system leverages OpenAI’s language models to power a variety of customer service, sentiment analysis, and data extraction features. Because pricing for these models is based on the number of tokens processed—and strict token limits apply—accurate token accounting is critical for managing costs and ensuring system stability.

    To optimize operational costs and prevent unexpected API overages, the engineering team at LexiSolve has developed an internal diagnostic tool that simulates and measures token usage for typical prompts sent to the language model.

    One specific test case an understanding of text tokenization. Your task is to generate data for that test case.

    Specifically, when you make a request to OpenAI's GPT-4o-Mini with just this user message:

    List only the valid English words from these: 9S044ch8e, WjEM8Js, XJBh, xS, b, phzdG, QzmcE, 5Iq4H, saT9xTT7D, hd4TjBsTC, Q, d37Sri119, 4w, 743, nP5Aso, X1, TDP1esuV9, bURqk, awi, 2, UXC1b, sdehKE, M, SD2VY, uyY, GUvd7xj, wITXH6l, 1Kpaw1LWM7, T3S, mnmyrEC3uj, wGZ, Mi, acsEJpGXmO, JLEcNucU, 1, fUuD6W, hEwNtHmGo, C, WIpzwv, JSHWYvp, RhNw, 2l, cD0hs1pc, P1gv, a7QpDiI, 1YjSa6, s, ONCGX, ibueZfnV8, hEqVvwVyxc, kHmvsOgT, sXzF4gz, VQfgntxAU, uBDCPG2ry, ZJup, 3Vgq5hQ, sV7S5, TqT, f3mk0er14A, ql, DpCy00, RmZD1Yf1Sn, gONas, WzIXJEwin, rCd, jdE, Fl5, es0KoP, V, RefeP, 6EXlPHoIE, Ezse3TfX, 7amGiIia, l3aJ253Wq7
    ... how many input tokens does it use up?

    Number of tokens:
    Remember: indicating that this is a user message takes up a few extra tokens. You actually need to make the request to get the answer.""",
    """RapidRoute Solutions is a logistics and delivery company that relies on accurate and standardized address data to optimize package routing. Recently, they encountered challenges with manually collecting and verifying new addresses for testing their planning software. To overcome this, the company decided to create an automated address generator using a language model, which would provide realistic, standardized U.S. addresses that could be directly integrated into their system.

    The engineering team at RapidRoute is tasked with designing a service that uses OpenAI's GPT-4o-Mini model to generate fake but plausible address data. The addresses must follow a strict format, which is critical for downstream processes such as geocoding, routing, and verification against customer databases. For consistency and validation, the development team requires that the addresses be returned as structured JSON data with no additional properties that could confuse their parsers.

    As part of the integration process, you need to write the body of the request to an OpenAI chat completion call that:

    Uses model gpt-4o-mini
    Has a system message: Respond in JSON
    Has a user message: Generate 10 random addresses in the US
    Uses structured outputs to respond with an object addresses which is an array of objects with required fields: county (string) zip (number) state (string) .
    Sets additionalProperties to false to prevent additional properties.
    Note that you don't need to run the request or use an API key; your task is simply to write the correct JSON body.

    What is the JSON body we should send to https://api.openai.com/v1/chat/completions for this? (No need to run it or to use an API key. Just write the body of the request below.)""",
    """Acme Global Solutions manages hundreds of invoices from vendors every month. To streamline their accounts payable process, the company is developing an automated document processing system. This system uses a computer vision model to extract useful text from scanned invoice images. Critical pieces of data such as vendor email addresses, invoice or transaction numbers, and other details are embedded within these documents.

    Your team is tasked with integrating OpenAI's vision model into the invoice processing workflow. The chosen model, gpt-4o-mini, is capable of analyzing both text and image inputs simultaneously. When an invoice is received—for example, an invoice image may contain a vendor email like alice.brown@acmeglobal.com and a transaction number such as 34921. The system needs to extract all embedded text to automatically populate the vendor management system.

    The automated process will send a POST request to OpenAI's API with two inputs in a single user message:

    Text: A simple instruction "Extract text from this image."
    Image URL: A base64 URL representing the invoice image that might include the email and the transaction number among other details.
    Here is an example invoice image:



    Write just the JSON body (not the URL, nor headers) for the POST request that sends these two pieces of content (text and image URL) to the OpenAI API endpoint.

    Use gpt-4o-mini as the model.
    Send a single user message to the model that has a text and an image_url content (in that order).
    The text content should be Extract text from this image.
    Send the image_url as a base64 URL of the image above. CAREFUL: Do not modify the image.
    Write your JSON body here:""",
    """SecurePay, a leading fintech startup, has implemented an innovative feature to detect and prevent fraudulent activities in real time. As part of its security suite, the system analyzes personalized transaction messages by converting them into embeddings. These embeddings are compared against known patterns of legitimate and fraudulent messages to flag unusual activity.

    Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized verification message to the user's registered email address. This message includes the user's email address and a unique transaction code (a randomly generated number). Here are 2 verification messages:

    Dear user, please verify your transaction code 68682 sent to 22f3000819@ds.study.iitm.ac.in
    Dear user, please verify your transaction code 8051 sent to 22f3000819@ds.study.iitm.ac.in
    The goal is to capture this message, convert it into a meaningful embedding using OpenAI's text-embedding-3-small model, and subsequently use the embedding in a machine learning model to detect anomalies.

    Your task is to write the JSON body for a POST request that will be sent to the OpenAI API endpoint to obtain the text embedding for the 2 given personalized transaction verification messages above. This will be sent to the endpoint https://api.openai.com/v1/embeddings.

    Write your JSON body here:""",
    """ShopSmart is an online retail platform that places a high value on customer feedback. Each month, the company receives hundreds of comments from shoppers regarding product quality, delivery speed, customer service, and more. To automatically understand and cluster this feedback, ShopSmart's data science team uses text embeddings to capture the semantic meaning behind each comment.

    As part of a pilot project, ShopSmart has curated a collection of 25 feedback phrases that represent a variety of customer sentiments. Examples of these phrases include comments like “Fast shipping and great service,” “Product quality could be improved,” “Excellent packaging,” and so on. Due to limited processing capacity during initial testing, you have been tasked with determine which pair(s) of 5 of these phrases are most similar to each other. This similarity analysis will help in grouping similar feedback to enhance the company’s understanding of recurring customer issues.

    ShopSmart has written a Python program that has the 5 phrases and their embeddings as an array of floats. It looks like this:

    embeddings = {"Customer service resolved my issue quickly.":[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136],"The item arrived damaged.":[0.04743589088320732,0.3924431800842285,-0.19287808239459991,0.0009346450679004192,-0.02529826946556568,0.007183298002928495,-0.12663501501083374,-0.1648762822151184,-0.09184173494577408,0.021719681099057198,-0.016338737681508064,0.1440839022397995,0.015228591859340668,-0.13091887533664703,-0.027949560433626175,0.14481529593467712,0.1035439744591713,-0.026539022102952003,-0.29924315214157104,0.04913375899195671,0.01723991520702839,0.14533771574497223,0.036674004048109055,-0.19653503596782684,-0.05490652099251747,-0.04375281557440758,0.25682249665260315,-0.1878628432750702,0.11273860186338425,0.08703545480966568,0.229447603225708,-0.07084038108587265,0.25891217589378357,-0.030300457030534744,0.018637394532561302,0.19883368909358978,-0.0997825413942337,0.2977803647518158,0.005384208634495735,0.03330438211560249,-0.07449733465909958,-0.022646980360150337,-0.07622132450342178,0.25598663091659546,-0.10782783478498459,0.12287358194589615,-0.02471054531633854,0.16644354164600372,-0.05433185398578644,-0.04077501222491264],"I found it hard to navigate the website.":[0.05301663279533386,-0.21206653118133545,-0.3240986168384552,-0.03143302723765373,0.12086819857358932,-0.12435400485992432,-0.1547534465789795,-0.07344505935907364,-0.16026587784290314,0.12265162914991379,-0.12467826157808304,-0.12411080300807953,-0.04150537773966789,0.026143522933125496,0.12581317126750946,0.0643252283334732,-0.0636361762881279,-0.08297022432088852,-0.2712441384792328,0.0668787807226181,0.23184643685817719,-0.03439190611243248,0.02334677428007126,0.07883589714765549,-0.07770098745822906,0.026042193174362183,-0.007098270580172539,0.09103620797395706,0.17801915109157562,0.051192667335271835,0.051760122179985046,-0.17737063765525818,0.16164399683475494,0.016608230769634247,-0.06947287172079086,-0.20606771111488342,0.13554099202156067,0.22228075563907623,0.19893397390842438,0.0876314714550972,0.03603347763419151,0.3054536283016205,0.34631049633026123,0.008765174075961113,-0.053057167679071426,0.09346816688776016,-0.18855763971805573,-0.05759681761264801,-0.03198021650314331,0.061325814574956894],"Great selection, but the size options were limited.":[0.11335355788469315,-0.06627686321735382,-0.05730358883738518,-0.1772221475839615,-0.190682053565979,-0.14000946283340454,-0.03737764060497284,0.0863017737865448,-0.22301223874092102,0.06462736427783966,-0.09197605401277542,-0.31960687041282654,-0.15175388753414154,0.0831347405910492,0.049550943076610565,0.012775368057191372,0.0678933709859848,-0.05585202947258949,-0.21390700340270996,0.144364133477211,0.024148661643266678,0.023455873131752014,0.00280002411454916,-0.10734938085079193,0.09131625294685364,-0.033814724534749985,-0.006305208895355463,0.012156805954873562,0.2611486613750458,0.13492900133132935,0.015051675960421562,-0.15597660839557648,-0.06363766640424728,-0.26695486903190613,-0.37318259477615356,0.018375417217612267,0.1467394083738327,0.13473105430603027,0.1976759284734726,0.14555177092552185,0.13235577940940857,-0.006663974840193987,0.15043428540229797,0.08029760420322418,0.20229452848434448,0.0745573416352272,-0.00456498796120286,-0.08656569570302963,-0.25006401538848877,-0.022977517917752266],"The quality exceeds the price.":[-0.050457071512937546,-0.034066375344991684,-0.10696785151958466,-0.03518003225326538,0.11867549270391464,-0.08566565811634064,-0.017789902165532112,0.3559122681617737,-0.04817265644669533,-0.14437519013881683,0.14620272815227509,0.015005768276751041,-0.34517550468444824,0.022687122225761414,0.2908063530921936,0.17681391537189484,-0.20993797481060028,-0.286237508058548,-0.022829897701740265,0.04428914561867714,0.08435212075710297,0.04840109869837761,-0.03081108257174492,-0.04203328490257263,-0.0324387289583683,-0.23552344739437103,0.0033713006414473057,0.02891216054558754,0.0676758736371994,-0.11616263538599014,0.05408358573913574,-0.18183964490890503,0.23757942020893097,-0.34266263246536255,-0.19920121133327484,-0.021787632256746292,0.0973161906003952,0.032724279910326004,0.07030294835567474,-0.1132500022649765,0.09360401332378387,0.028341054916381836,-0.09657375514507294,0.1291838139295578,0.12198790162801743,0.019260495901107788,0.02211601845920086,0.058595310896635056,-0.07481467723846436,0.012935514561831951]}
    Your task is to write a Python function most_similar(embeddings) that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar.

    Write your Python code here:""",
    """InfoCore Solutions is a technology consulting firm that maintains an extensive internal knowledge base of technical documents, project reports, and case studies. Employees frequently search through these documents to answer client questions quickly or gain insights for ongoing projects. However, due to the sheer volume of documentation, traditional keyword-based search often returns too many irrelevant results.

    To address this issue, InfoCore's data science team decides to integrate a semantic search feature into their internal portal. This feature uses text embeddings to capture the contextual meaning of both the documents and the user's query. The documents are pre-embedded, and when an employee submits a search query, the system computes the similarity between the query's embedding and those of the documents. The API then returns a ranked list of document identifiers based on similarity.

    Imagine you are an engineer on the InfoCore team. Your task is to build a FastAPI POST endpoint that accepts an array of docs and query string via a JSON body. The endpoint is structured as follows:

    POST /similarity

    {
    "docs": ["Contents of document 1", "Contents of document 2", "Contents of document 3", ...],
    "query": "Your query string"
    }
    Service Flow:

    Request Payload: The client sends a POST request with a JSON body containing:
    docs: An array of document texts from the internal knowledge base.
    query: A string representing the user's search query.
    Embedding Generation: For each document in the docs array and for the query string, the API computes a text embedding using text-embedding-3-small.
    Similarity Computation: The API then calculates the cosine similarity between the query embedding and each document embedding. This allows the service to determine which documents best match the intent of the query.
    Response Structure: After ranking the documents by their similarity scores, the API returns the identifiers (or positions) of the three most similar documents. The JSON response might look like this:

    {
    "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
    }
    Here, "Contents of document 3" is considered the closest match, followed by "Contents of document 1", then "Contents of document 2".

    Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers.

    What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity
    We'll check by sending a POST request to this URL with a JSON body containing random docs and query.""",
    """TechNova Corp. is a multinational corporation that has implemented a digital assistant to support employees with various internal tasks. The assistant can answer queries related to human resources, IT support, and administrative services. Employees use a simple web interface to enter their requests, which may include:

    Checking the status of an IT support ticket.
    Scheduling a meeting.
    Retrieving their current expense reimbursement balance.
    Requesting details about their performance bonus.
    Reporting an office issue by specifying a department or issue number.
    Each question is direct and templatized, containing one or more parameters such as an employee or ticket number (which might be randomized). In the backend, a FastAPI app routes each request by matching the query to one of a set of pre-defined functions. The response that the API returns is used by OpenAI to call the right function with the necessary arguments.

    Pre-Defined Functions:

    For this exercise, assume the following functions have been defined:

    get_ticket_status(ticket_id: int)
    schedule_meeting(date: str, time: str, meeting_room: str)
    get_expense_balance(employee_id: int)
    calculate_performance_bonus(employee_id: int, current_year: int)
    report_office_issue(issue_code: int, department: str)
    Each function has a specific signature, and the student’s FastAPI app should map specific queries to these functions.

    Example Questions (Templatized with a Random Number):

    Ticket Status:
    Query: "What is the status of ticket 83742?"
    → Should map to get_ticket_status(ticket_id=83742)
    Meeting Scheduling:
    Query: "Schedule a meeting on 2025-02-15 at 14:00 in Room A."
    → Should map to schedule_meeting(date="2025-02-15", time="14:00", meeting_room="Room A")
    Expense Reimbursement:
    Query: "Show my expense balance for employee 10056."
    → Should map to get_expense_balance(employee_id=10056)
    Performance Bonus Calculation:
    Query: "Calculate performance bonus for employee 10056 for 2025."
    → Should map to calculate_performance_bonus(employee_id=10056, current_year=2025)
    Office Issue Reporting:
    Query: "Report office issue 45321 for the Facilities department."
    → Should map to report_office_issue(issue_code=45321, department="Facilities")
    Task Overview:

    Develop a FastAPI application that:

    Exposes a GET endpoint /execute?q=... where the query parameter q contains one of the pre-templatized questions.
    Analyzes the q parameter to identify which function should be called.
    Extracts the parameters from the question text.
    Returns a response in the following JSON format:

    { "name": "function_name", "arguments": "{ ...JSON encoded parameters... }" }
    For example, the query "What is the status of ticket 83742?" should return:

    {
    "name": "get_ticket_status",
    "arguments": "{\"ticket_id\": 83742}"
    }
    Make sure you enable CORS to allow GET requests from any origin.

    What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute
    We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition."""
]

ga4questions = [
    """Sports Analytics for CricketPro
    CricketPro Insights is a leading sports analytics firm specializing in providing in-depth statistical analysis and insights for cricket teams, coaches, and enthusiasts. Leveraging data from prominent sources like ESPN Cricinfo, CricketPro offers actionable intelligence that helps teams optimize player performance, strategize game plans, and engage with fans through detailed statistics and visualizations.

    In the competitive world of cricket, understanding player performance metrics is crucial for team selection, game strategy, and player development. However, manually extracting and analyzing batting statistics from extensive datasets spread across multiple web pages is time-consuming and prone to errors. To maintain their edge and deliver timely insights, CricketPro needs an efficient, automated solution to aggregate and analyze player performance data from ESPN Cricinfo's ODI (One Day International) batting statistics.

    CricketPro Insights has identified the need to automate the extraction and analysis of ODI batting statistics from ESPN Cricinfo to streamline their data processing workflow. The statistics are available on a paginated website, with each page containing a subset of player data. By automating this process, CricketPro aims to provide up-to-date insights on player performances, such as the number of duck outs (i.e. a score of zero), which are pivotal for team assessments and strategic planning.

    As part of this initiative, you are tasked with developing a solution that allows CricketPro analysts to:

    Navigate Paginated Data: Access specific pages of the ODI batting statistics based on varying requirements.
    Extract Relevant Data: Use Google Sheets' IMPORTHTML function to pull tabular data from ESPN Cricinfo.
    Analyze Performance Metrics: Count the number of ducks (where the player was out for 0 runs) each player has, aiding in performance evaluations.
    Your Task
    ESPN Cricinfo has ODI batting stats for each batsman. The result is paginated across multiple pages. Count the number of ducks in page number 37.

    Understanding the Data Source: ESPN Cricinfo's ODI batting statistics are spread across multiple pages, each containing a table of player data. Go to page number 37.
    Setting Up Google Sheets: Utilize Google Sheets' IMPORTHTML function to import table data from the URL for page number 37.
    Data Extraction and Analysis: Pull the relevant table from the assigned page into Google Sheets. Locate the column that represents the number of ducks for each player. (It is titled "0".) Sum the values in the "0" column to determine the total number of ducks on that page.
    Impact
    By automating the extraction and analysis of cricket batting statistics, CricketPro Insights can:

    Enhance Analytical Efficiency: Reduce the time and effort required to manually gather and process player performance data.
    Provide Timely Insights: Deliver up-to-date statistical analyses that aid teams and coaches in making informed decisions.
    Scalability: Easily handle large volumes of data across multiple pages, ensuring comprehensive coverage of player performances.
    Data-Driven Strategies: Enable the development of data-driven strategies for player selection, training focus areas, and game planning.
    Client Satisfaction: Improve service offerings by providing accurate and insightful analytics that meet the specific needs of clients in the cricketing world.
    What is the total number of ducks across players on page number 37 of ESPN Cricinfo's ODI batting stats?""",
    """Content Curation for StreamFlix Streaming
    StreamFlix is a rapidly growing streaming service aiming to provide a diverse and high-quality library of movies, TV shows, etc. to its subscribers. To maintain a competitive edge and ensure customer satisfaction, StreamFlix invests heavily in data-driven content curation. By analyzing movie ratings and other key metrics, the company seeks to identify films that align with subscriber preferences and emerging viewing trends.

    With millions of titles available on platforms like IMDb, manually sifting through titles to select suitable additions to StreamFlix's catalog is both time-consuming and inefficient. To streamline this process, StreamFlix's data analytics team requires an automated solution to extract and analyze movie data based on specific rating criteria.

    Develop a Python program that interacts with IMDb's dataset to extract detailed information about titles within a specified rating range. The extracted data should include the movie's unique ID, title, release year, and rating. This information will be used to inform content acquisition decisions, ensuring that StreamFlix consistently offers high-quality and well-received films to its audience.

    Imagine you are a data analyst at StreamFlix, responsible for expanding the platform's movie library. Your task is to identify titles that have received favorable ratings on IMDb, ensuring that the selected titles meet the company's quality standards and resonate with subscribers.

    To achieve this, you need to:

    Extract Data: Retrieve movie information from IMDb for all films that have a rating between 3 and 8.
    Format Data: Structure the extracted information into a JSON format containing the following fields:
    id: The unique identifier for the movie on IMDb.
    title: The official title of the movie.
    year: The year the movie was released.
    rating: The IMDb user rating for the movie.
    Your Task
    Source: Utilize IMDb's advanced web search at https://www.imdb.com/search/title/ to access movie data.
    Filter: Filter all titles with a rating between 3 and 8.
    Format: For up to the first 25 titles, extract the necessary details: ID, title, year, and rating. The ID of the movie is the part of the URL after tt in the href attribute. For example, tt10078772. Organize the data into a JSON structure as follows:

    [
    { "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
    { "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },
    // ... more titles
    ]
    Submit: Submit the JSON data in the text box below.
    Impact
    By completing this assignment, you'll simulate a key component of a streaming service's content acquisition strategy. Your work will enable StreamFlix to make informed decisions about which titles to license, ensuring that their catalog remains both diverse and aligned with subscriber preferences. This, in turn, contributes to improved customer satisfaction and retention, driving the company's growth and success in a competitive market.

    What is the JSON data?
    IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code.""",
    """A Country Information API for GlobalEdu
    GlobalEdu Platforms is a leading provider of educational technology solutions, specializing in creating interactive and informative content for students and educators worldwide. Their suite of products includes digital textbooks, educational apps, and online learning platforms that aim to make learning more engaging and accessible. To enhance their offerings, GlobalEdu Platforms seeks to integrate comprehensive country information into their educational tools, enabling users to access structured and easily navigable content about various nations.

    With the vast amount of information available on platforms like Wikipedia, manually curating and organizing country-specific data for educational purposes is both time-consuming and inefficient. GlobalEdu Platforms aims to automate this process to ensure that their educational materials are up-to-date, accurate, and well-structured. The key challenges they face include:

    Content Organization: Presenting information in a structured and hierarchical manner that aligns with educational standards.
    Scalability: Handling data for a large number of countries without manual intervention.
    Accessibility: Ensuring that the information is easily accessible from various applications and platforms used by educators and students.
    Interoperability: Allowing cross-origin requests to integrate the API seamlessly with different front-end applications.
    To address these challenges, GlobalEdu Platforms has decided to develop a web application that exposes a RESTful API. This API will allow their educational tools to fetch and display structured outlines of Wikipedia pages for any given country. The application needs to:

    Accept a country name as a query parameter.
    Fetch the corresponding Wikipedia page for that country.
    Extract all headings (H1 to H6) from the page.
    Generate a Markdown-formatted outline that reflects the hierarchical structure of the content.
    Enable Cross-Origin Resource Sharing (CORS) to allow GET requests from any origin, facilitating seamless integration with various educational platforms.
    Your Task
    Write a web application that exposes an API with a single query parameter: ?country=. It should fetch the Wikipedia page of the country, extracts all headings (H1 to H6), and create a Markdown outline for the country. The outline should look like this:


    ## Contents

    # Vanuatu

    ## Etymology

    ## History

    ### Prehistory

    ...
    API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that accepts a country query parameter.
    Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML.
    Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, lxml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6) from the page, maintaining order.
    Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #.
    Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.
    What is the URL of your API endpoint?
    We'll check by sending a request to this URL with ?country=... passing different countries.""",
    """Weather Data Integration for AgroTech Insights
    AgroTech Insights is a leading agricultural technology company that provides data-driven solutions to farmers and agribusinesses. By leveraging advanced analytics and real-time data, AgroTech helps optimize crop yields, manage resources efficiently, and mitigate risks associated with adverse weather conditions. Accurate and timely weather forecasts are crucial for making informed decisions in agricultural planning and management.

    Farmers and agribusinesses rely heavily on precise weather information to plan planting schedules, irrigation, harvesting, and protect crops from extreme weather events. However, accessing and processing weather data from multiple sources can be time-consuming and technically challenging. AgroTech Insights seeks to automate the extraction and transformation of weather data to provide seamless, actionable insights to its clients.

    AgroTech Insights has partnered with various stakeholders to enhance its weather forecasting capabilities. One of the key requirements is to integrate weather forecast data for specific regions to support crop management strategies. For this purpose, AgroTech utilizes the BBC Weather API, a reliable source of detailed weather information.

    Your Task
    As part of this initiative, you are tasked with developing a system that automates the following:

    API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Istanbul. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city).
    Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId.
    Data Transformation: Extract the localDate and enhancedWeatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each localDate to its corresponding enhancedWeatherDescription. Create a JSON object where each key is the localDate and the value is the enhancedWeatherDescription.
    The output would look like this:

    {
    "2025-01-01": "Sunny with scattered clouds",
    "2025-01-02": "Partly cloudy with a chance of rain",
    "2025-01-03": "Overcast skies",
    // ... additional days
    }
    What is the JSON weather forecast description for Istanbul?""",
    """Geospatial Data Optimization for UrbanRide
    UrbanRide is a leading transportation and logistics company operating in major metropolitan areas worldwide. To enhance their service efficiency, optimize route planning, and improve customer satisfaction, UrbanRide relies heavily on accurate geospatial data. Precise bounding box information of cities helps in defining service zones, managing fleet distribution, and analyzing regional demand patterns.

    As UrbanRide expands into new cities, the company faces the challenge of accurately delineating service areas within these urban environments. Defining the geographical boundaries of a city is crucial for:

    Route Optimization: Ensuring drivers operate within designated zones to minimize transit times and fuel consumption.
    Fleet Management: Allocating vehicles effectively across different regions based on demand and service coverage.
    Market Analysis: Understanding regional demand to tailor services and promotional efforts accordingly.
    However, manually extracting and verifying bounding box data for each city is time-consuming and prone to inconsistencies, especially when dealing with cities that share names across different countries or have multiple administrative districts.

    UrbanRide’s data analytics team needs to automate the extraction of precise bounding box coordinates (specifically the minimum and maximum latitude) for various populous cities across different countries. This automation ensures consistency, accuracy, and scalability as the company grows its operations.

    To achieve this, the team utilizes the Nominatim API, a geocoding service based on OpenStreetMap data, to programmatically retrieve geospatial information. However, challenges arise when cities with the same name exist in multiple countries or have multiple entries within the same country. To address this, the team must implement a method to select the correct city instance based on specific identifiers (e.g., osm_id patterns).

    Your Task
    What is the maximum latitude of the bounding box of the city Santiago in the country Chile on the Nominatim API?

    API Integration: Use the Nominatim API to fetch geospatial data for a specified city within a country via a GET request to the Nominatim API with parameters for the city and country. Ensure adherence to Nominatim’s usage policies, including rate limiting and proper attribution.
    Data Retrieval and Filtering: Parse the JSON response from the API. If multiple results are returned (e.g., multiple cities named “Springfield” in different states), filter the results based on the provided osm_id ending to select the correct city instance.
    Parameter Extraction: Access the boundingbox attribute. Depending on whether you're looking for the minimum or maximum latitude, extract the corresponding latitude value.
    Impact
    By automating the extraction and processing of bounding box data, UrbanRide can:

    Optimize Routing: Enhance route planning algorithms with precise geographical boundaries, reducing delivery times and operational costs.
    Improve Fleet Allocation: Allocate vehicles more effectively across defined service zones based on accurate city extents.
    Enhance Market Analysis: Gain deeper insights into regional performance, enabling targeted marketing and service improvements.
    Scale Operations: Seamlessly integrate new cities into their service network with minimal manual intervention, ensuring consistent data quality.
    What is the maximum latitude of the bounding box of the city Santiago in the country Chile on the Nominatim API? Value of the maximum latitude""",
    """Media Intelligence for TechInsight Analytics
    TechInsight Analytics is a leading market research firm specializing in technology trends and media intelligence. The company provides actionable insights to tech companies, startups, and investors by analyzing online discussions, news articles, and social media posts. One of their key data sources is Hacker News, a popular platform where tech enthusiasts and professionals share and discuss the latest in technology, startups, and innovation.

    In the rapidly evolving tech landscape, staying updated with the latest trends and public sentiments is crucial for TechInsight Analytics' clients. Manual monitoring of Hacker News posts for specific topics and engagement levels is inefficient and error-prone due to the high volume of daily posts. To address this, TechInsight seeks to automate the process of identifying and extracting relevant Hacker News posts that mention specific technology topics and have garnered significant attention (measured by points).

    TechInsight Analytics has developed an internal tool that leverages the HNRSS API to fetch the latest Hacker News posts. The tool needs to perform the following tasks:

    Topic Monitoring: Continuously monitor Hacker News for posts related to specific technology topics, such as "Artificial Intelligence," "Blockchain," or "Cybersecurity."
    Engagement Filtering: Identify posts that have received a minimum number of points (votes) to ensure the content is highly engaging and relevant.
    Data Extraction: Extract essential details from the qualifying posts, including the post's link for further analysis and reporting.
    To achieve this, the team needs to create a program that:

    Searches Hacker News for the latest posts mentioning a specified topic.
    Filters these posts based on a minimum points threshold.
    Retrieves and returns the link to the most relevant post.
    Your Task
    Search using the Hacker News RSS API for the latest Hacker News post mentioning Quantum Computing and having a minimum of 67 points. What is the link that it points to?

    Automate Data Retrieval: Utilize the HNRSS API to fetch the latest Hacker News posts. Use the URL relevant to fetching the latest posts, searching for topics and filtering by a minimum number of points.
    Extract and Present Data: Extract the most recent <item> from this result. Get the <link> tag inside it.
    Share the result: Type in just the URL in the answer.
    What is the link to the latest Hacker News post mentioning Quantum Computing having at least 67 points?"""
    """Emerging Developer Talent for CodeConnect
    CodeConnect is an innovative recruitment platform that specializes in matching high-potential tech talent with forward-thinking companies. As the demand for skilled software developers grows, CodeConnect is committed to staying ahead of trends by leveraging data-driven insights to identify emerging developers—especially those who demonstrate strong community influence on platforms like GitHub.

    For CodeConnect, a key objective is to tap into regional talent pools to support local hiring initiatives and foster diversity within tech teams. One specific challenge is identifying developers in major tech hubs (such as Shanghai) who not only have established GitHub profiles but also show early signs of influence, as indicated by their follower counts.

    However, with millions of developers on GitHub and constantly evolving profiles, manually filtering through the data is impractical. CodeConnect needs an automated solution that:

    Filters Developer Profiles: Retrieves GitHub users based on location and a minimum follower threshold (e.g., over 60 followers) to focus on those with some level of social proof.
    Identifies the Newest Talent: Determines the most recent GitHub user in the selected group, providing insight into new emerging talent.
    Standardizes Data: Returns the account creation date in a standardized ISO 8601 format, ensuring consistent reporting across the organization.
    The recruitment team at CodeConnect is launching a new initiative aimed at hiring young, promising developers in Shanghai—a city known for its vibrant tech community. To support this initiative, the team has commissioned a project to use the GitHub API to find all users located in Shanghai with more than 60 followers. From this filtered list, they need to identify the newest account based on the profile creation date. This information will help the team target outreach efforts to developers who have recently joined the platform and may be eager to explore new career opportunities.

    Your Task
    Using the GitHub API, find all users located in the city Chicago with over 70 followers.

    When was the newest user's GitHub profile created?

    API Integration and Data Retrieval: Leverage GitHub’s search endpoints to query users by location and filter them by follower count.
    Data Processing: From the returned list of GitHub users, isolate those profiles that meet the specified criteria.
    Sort and Format: Identify the "newest" user by comparing the created_at dates provided in the user profile data. Format the account creation date in the ISO 8601 standard (e.g., "2024-01-01T00:00:00Z").
    Impact
    By automating this data retrieval and filtering process, CodeConnect gains several strategic advantages:

    Targeted Recruitment: Quickly identify new, promising talent in key regions, allowing for more focused and timely recruitment campaigns.
    Competitive Intelligence: Stay updated on emerging trends within local developer communities and adjust talent acquisition strategies accordingly.
    Efficiency: Automating repetitive data collection tasks frees up time for recruiters to focus on engagement and relationship-building.
    Data-Driven Decisions: Leverage standardized and reliable data to support strategic business decisions in recruitment and market research.
    Enter the date (ISO 8601, e.g. "2024-01-01T00:00:00Z") when the newest user joined GitHub.
    Search using location: and followers: filters, sort by joined descending, fetch the first url, and enter the created_at field. Ignore ultra-new users who JUST joined, i.e. after 3/25/2025, 2:14:02 AM.""",
    """Emerging Developer Talent for CodeConnect
    CodeConnect is an innovative recruitment platform that specializes in matching high-potential tech talent with forward-thinking companies. As the demand for skilled software developers grows, CodeConnect is committed to staying ahead of trends by leveraging data-driven insights to identify emerging developers—especially those who demonstrate strong community influence on platforms like GitHub.

    For CodeConnect, a key objective is to tap into regional talent pools to support local hiring initiatives and foster diversity within tech teams. One specific challenge is identifying developers in major tech hubs (such as Shanghai) who not only have established GitHub profiles but also show early signs of influence, as indicated by their follower counts.

    However, with millions of developers on GitHub and constantly evolving profiles, manually filtering through the data is impractical. CodeConnect needs an automated solution that:

    Filters Developer Profiles: Retrieves GitHub users based on location and a minimum follower threshold (e.g., over 60 followers) to focus on those with some level of social proof.
    Identifies the Newest Talent: Determines the most recent GitHub user in the selected group, providing insight into new emerging talent.
    Standardizes Data: Returns the account creation date in a standardized ISO 8601 format, ensuring consistent reporting across the organization.
    The recruitment team at CodeConnect is launching a new initiative aimed at hiring young, promising developers in Shanghai—a city known for its vibrant tech community. To support this initiative, the team has commissioned a project to use the GitHub API to find all users located in Shanghai with more than 60 followers. From this filtered list, they need to identify the newest account based on the profile creation date. This information will help the team target outreach efforts to developers who have recently joined the platform and may be eager to explore new career opportunities.

    Your Task
    Using the GitHub API, find all users located in the city Chicago with over 70 followers.

    When was the newest user's GitHub profile created?

    API Integration and Data Retrieval: Leverage GitHub’s search endpoints to query users by location and filter them by follower count.
    Data Processing: From the returned list of GitHub users, isolate those profiles that meet the specified criteria.
    Sort and Format: Identify the "newest" user by comparing the created_at dates provided in the user profile data. Format the account creation date in the ISO 8601 standard (e.g., "2024-01-01T00:00:00Z").
    Impact
    By automating this data retrieval and filtering process, CodeConnect gains several strategic advantages:

    Targeted Recruitment: Quickly identify new, promising talent in key regions, allowing for more focused and timely recruitment campaigns.
    Competitive Intelligence: Stay updated on emerging trends within local developer communities and adjust talent acquisition strategies accordingly.
    Efficiency: Automating repetitive data collection tasks frees up time for recruiters to focus on engagement and relationship-building.
    Data-Driven Decisions: Leverage standardized and reliable data to support strategic business decisions in recruitment and market research.
    Enter the date (ISO 8601, e.g. "2024-01-01T00:00:00Z") when the newest user joined GitHub.
    Search using location: and followers: filters, sort by joined descending, fetch the first url, and enter the created_at field. Ignore ultra-new users who JUST joined, i.e. after 3/25/2025, 3:55:48 AM.""",
    """Automating Repository Updates for DevSync
    DevSync Solutions is a mid-sized software development company specializing in collaborative tools for remote teams. With a growing client base and an expanding portfolio of projects, DevSync emphasizes efficient workflow management and robust version control practices to maintain high-quality software delivery.

    As part of their commitment to maintaining seamless and transparent development processes, DevSync has identified the need to implement automated daily updates to their GitHub repositories. These updates serve multiple purposes:

    Activity Tracking: Ensuring that each repository reflects daily activity helps in monitoring project progress and team engagement.
    Automated Documentation: Regular commits can be used to update status files, logs, or documentation without manual intervention.
    Backup and Recovery: Automated commits provide an additional layer of backup, ensuring that changes are consistently recorded.
    Compliance and Auditing: Maintaining a clear commit history aids in compliance with industry standards and facilitates auditing processes.
    Manually managing these daily commits is inefficient and prone to human error, especially as the number of repositories grows. To address this, DevSync seeks to automate the process using GitHub Actions, ensuring consistency, reliability, and scalability across all projects.

    DevSync's DevOps team has decided to standardize the implementation of GitHub Actions across all company repositories. The objective is to create a scheduled workflow that runs once daily, adds a commit to the repository, and ensures that these actions are consistently tracked and verifiable.

    As a junior developer or DevOps engineer at DevSync, you are tasked with setting up this automation for a specific repository. This exercise will not only enhance your understanding of GitHub Actions but also contribute to the company's streamlined workflow management.

    Your Task
    Create a scheduled GitHub action that runs daily and adds a commit to your repository. The workflow should:

    Use schedule with cron syntax to run once per day (must use specific hours/minutes, not wildcards)
    Include a step with your email 22f3000819@ds.study.iitm.ac.in in its name
    Create a commit in each run
    Be located in .github/workflows/ directory
    After creating the workflow:

    Trigger the workflow and wait for it to complete
    Ensure it appears as the most recent action in your repository
    Verify that it creates a commit during or within 5 minutes of the workflow run
    Enter your repository URL (format: https://github.com/USER/REPO):""",
    """Academic Performance Analysis for EduAnalytics
    EduAnalytics Corp. is a leading educational technology company that partners with schools and educational institutions to provide data-driven insights into student performance. By leveraging advanced analytics and reporting tools, EduAnalytics helps educators identify trends, improve teaching strategies, and enhance overall student outcomes. One of their key offerings is the Performance Insight Dashboard, which aggregates and analyzes student marks across various subjects and demographic groups.

    EduAnalytics has recently onboarded Greenwood High School, a large educational institution aiming to optimize its teaching methods and improve student performance in core subjects. Greenwood High School conducts annual assessments in multiple subjects, and the results are compiled into detailed PDF reports each semester. However, manually extracting and analyzing this data is time-consuming and prone to errors, especially given the volume of data and the need for timely insights.

    To address this, EduAnalytics plans to automate the data extraction and analysis process, enabling Greenwood High School to receive precise and actionable reports without the delays associated with manual processing.

    As part of this initiative, you are a data analyst at EduAnalytics assigned to develop a module that processes PDF reports containing student marks. Each PDF, named in the format xxx.pdf, includes a comprehensive table listing student performances across various subjects, along with their respective groups.

    Greenwood High School has specific analytical needs, such as:

    Subject Performance Analysis: Understanding how students perform in different subjects to identify areas needing improvement.
    Group-Based Insights: Analyzing performance across different student groups to ensure equitable educational support.
    Threshold-Based Reporting: Focusing on students who meet or exceed certain performance thresholds to tailor advanced programs or interventions.
    Your Task
    This file,  contains a table of student marks in Maths, Physics, English, Economics, and Biology.

    Calculate the total Maths marks of students who scored 51 or more marks in Physics in groups 1-22 (including both groups).

    Data Extraction:: Retrieve the PDF file containing the student marks table and use PDF parsing libraries (e.g., Tabula, Camelot, or PyPDF2) to accurately extract the table data into a workable format (e.g., CSV, Excel, or a DataFrame).
    Data Cleaning and Preparation: Convert marks to numerical data types to facilitate accurate calculations.
    Data Filtering: Identify students who have scored marks between 51 and Physics in groups 1-22 (including both groups).
    Calculation: Sum the marks of the filtered students to obtain the total marks for this specific cohort.
    By automating the extraction and analysis of student marks, EduAnalytics empowers Greenwood High School to make informed decisions swiftly. This capability enables the school to:

    Identify Performance Trends: Quickly spot areas where students excel or need additional support.
    Allocate Resources Effectively: Direct teaching resources and interventions to groups and subjects that require attention.
    Enhance Reporting Efficiency: Reduce the time and effort spent on manual data processing, allowing educators to focus more on teaching and student engagement.
    Support Data-Driven Strategies: Use accurate and timely data to shape educational strategies and improve overall student outcomes.
    What is the total Maths marks of students who scored 51 or more marks in Physics in groups 1-22 (including both groups)?""",
    """Digital Documentation Transformation for EduDocs Inc.
    EduDocs Inc. is a leading provider of educational resources and documentation management solutions for academic institutions. With a growing client base comprising universities, colleges, and online learning platforms, EduDocs emphasizes the importance of accessible, well-formatted digital documentation. To maintain high standards and streamline their content delivery, EduDocs continually seeks to enhance its documentation workflows and ensure consistency across all materials.

    EduDocs manages a vast repository of educational materials, including course syllabi, lecture notes, research papers, and administrative documents. These materials are often provided by clients in various formats, predominantly PDF, which poses challenges for content reuse, editing, and integration into digital platforms.

    Manually converting PDF documents to Markdown is time-consuming and prone to errors, especially when dealing with large volumes of documents. Additionally, ensuring that the converted Markdown adheres to consistent formatting standards is crucial for maintaining the professional quality of EduDocs' deliverables.

    To address these challenges, EduDocs aims to automate and standardize the conversion of PDF documents to Markdown format, ensuring that all Markdown files are consistently formatted using Prettier 3.4.2. This initiative will improve efficiency, reduce manual effort, and enhance the overall quality of the documentation provided to clients.

    Your Task
    As part of the Documentation Transformation Project, you are a junior developer at EduDocs tasked with developing a streamlined workflow for converting PDF files to Markdown and ensuring their consistent formatting. This project is critical for supporting EduDocs' commitment to delivering high-quality, accessible educational resources to its clients.

    has the contents of a sample document.

    Convert the PDF to Markdown: Extract the content from the PDF file. Accurately convert the extracted content into Markdown format, preserving the structure and formatting as much as possible.
    Format the Markdown: Use Prettier version 3.4.2 to format the converted Markdown file.
    Submit the Formatted Markdown: Provide the final, formatted Markdown file as your submission.
    Impact
    By completing this exercise, you will contribute to EduDocs Inc.'s mission of providing high-quality, accessible educational resources. Automating the PDF to Markdown conversion and ensuring consistent formatting:

    Enhances Productivity: Reduces the time and effort required to prepare documentation for clients.
    Improves Quality: Ensures all documents adhere to standardized formatting, enhancing readability and professionalism.
    Supports Scalability: Enables EduDocs to handle larger volumes of documentation without compromising on quality.
    Facilitates Integration: Makes it easier to integrate Markdown-formatted documents into various digital platforms and content management systems.
    What is the markdown content of the PDF, formatted with prettier@3.4.2?
    It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things."""
]

ga5questions = [
    """Improving Sales Data Accuracy for RetailWise Inc.
    RetailWise Inc. is a retail analytics firm that supports companies in optimizing their pricing, margins, and inventory decisions. Their reports depend on accurate historical sales data, but legacy data sources are often messy. Recently, RetailWise received an Excel sheet containing 1,000 transaction records that were generated from scanned receipts. Due to OCR inconsistencies and legacy formatting issues, the data in the Excel sheet is not clean.

    The Excel file has these columns, and they are messy:

    Customer Name: Contains leading/trailing spaces.
    Country: Uses inconsistent representations. Instead of 2-letter abbreviations, it also contains other values like "USA" vs. "US", "UK" vs. "U.K", "Fra" for France, "Bra" for Brazil, "Ind" for India.
    Date: Uses mixed formats like "MM-DD-YYYY", "YYYY/MM/DD", etc.
    Product: Includes a product name followed by a slash and a random code (e.g., "Theta/5x01vd"). Only the product name part (before the slash) is relevant.
    Sales and Cost: Contain extra spaces and the currency string ("USD"). In some rows, the Cost field is missing. When the cost is missing, it should be treated as 50% of the Sales value.
    TransactionID: Though formatted as four-digit numbers, this field may have inconsistent spacing.
    Your Task
    You need to clean this Excel data and calculate the total margin for all transactions that satisfy the following criteria:

    Time Filter: Sales that occurred up to and including a specified date (Fri Apr 01 2022 11:41:29 GMT+0530 (India Standard Time)).
    Product Filter: Transactions for a specific product (Iota). (Use only the product name before the slash.)
    Country Filter: Transactions from a specific country (IN), after standardizing the country names.
    The total margin is defined as:

    Total Margin
    =
    Total Sales
    −
    Total Cost
    Total Sales

    Your solution should address the following challenges:

    Trim and Normalize Strings: Remove extra spaces from the Customer Name and Country fields. Map inconsistent country names (e.g., "USA", "U.S.A", "US") to a standardized format.
    Standardize Date Formats: Detect and convert dates from "MM-DD-YYYY" and "YYYY/MM/DD" into a consistent date format (e.g., ISO 8601).
    Extract the Product Name: From the Product field, extract the portion before the slash (e.g., extract "Theta" from "Theta/5x01vd").
    Clean and Convert Sales and Cost: Remove the "USD" text and extra spaces from the Sales and Cost fields. Convert these fields to numerical values. Handle missing Cost values appropriately (50% of Sales).
    Filter the Data: Include only transactions up to and including Fri Apr 01 2022 11:41:29 GMT+0530 (India Standard Time), matching product Iota, and country IN.
    Calculate the Margin: Sum the Sales and Cost for the filtered transactions. Compute the overall margin using the formula provided.
    By cleaning the data and calculating accurate margins, RetailWise Inc. can:

    Improve Decision Making: Provide clients with reliable margin analyses to optimize pricing and inventory.
    Enhance Reporting: Ensure historical data is consistent and accurate, boosting stakeholder confidence.
    Streamline Operations: Reduce the manual effort needed to clean data from legacy sources.
    Download the Sales Excel file: 

    What is the total margin for transactions before Fri Apr 01 2022 11:41:29 GMT+0530 (India Standard Time) for Iota sold in IN (which may be spelt in different ways)?
    You can enter the margin as a percentage (e.g. 12.34%) or a decimal (e.g. 0.1234).""",
    """Streamlining Student Records for EduTrack
    EduTrack Systems is a leading provider of educational management software that helps schools and universities maintain accurate and up-to-date student records. EduTrack's platform is used by administrators to monitor academic performance, manage enrollment, and generate reports for compliance and strategic planning.

    In many educational institutions, student data is collected from multiple sources—such as handwritten forms, scanned documents, and digital submissions—which can lead to duplicate records. These duplicates cause inefficiencies in reporting and can lead to incorrect decision-making when it comes to resource allocation, student support, and performance analysis.

    Recently, EduTrack received a text file containing student exam results that were processed through Optical Character Recognition (OCR) from legacy documents. The file is formatted with lines structured as follows:

    NAME STUDENT ID Marks MARKS

    Alice  - A293:Marks 32

    Bob - BD29DMarks 53

    Charlie - XF28:Marks40
    The data spans multiple subjects and time periods. The file will contain duplicate entries for the same student (identified by the second field), and it is crucial to count only unique students for accurate reporting.

    Your Task
    As a data analyst at EduTrack Systems, your task is to process this text file and determine the number of unique students based on their student IDs. This deduplication is essential to:

    Ensure Accurate Reporting: Avoid inflated counts in enrollment and performance reports.
    Improve Data Quality: Clean the dataset for further analytics, such as tracking academic progress or resource allocation.
    Optimize Administrative Processes: Provide administrators with reliable data to support decision-making.
    You need to do the following:

    Data Extraction: Read the text file line by line. Parse each line to extract the student ID.
    Deduplication: Remove duplicates from the student ID list.
    Reporting: Count the number of unique student IDs present in the file.
    By accurately identifying the number of unique students, EduTrack Systems will:

    Enhance Data Integrity: Ensure that subsequent analyses and reports reflect the true number of individual students.
    Reduce Administrative Errors: Minimize the risk of misinformed decisions that can arise from duplicate entries.
    Streamline Resource Allocation: Provide accurate student counts for budgeting, staffing, and planning academic programs.
    Improve Compliance Reporting: Ensure adherence to regulatory requirements by maintaining precise student records.
    Download the text file with student marks 

    How many unique students are there in the file?""",
    """Peak Usage Analysis for Regional Content
    s-anand.net is a personal website that had region-specific music content. One of the site's key sections is telugu, which hosts music files and is especially popular among the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server load, and content engagement.

    The author noticed unusual traffic patterns during weekend evenings. To better tailor their content and optimize server resources, they need to know precisely how many successful requests are made to the telugu section during peak hours on Monday. Specifically, they are interested in:

    Time Window: From 11 until before 20.
    Request Type: Only GET requests.
    Success Criteria: Requests that return HTTP status codes between 200 and 299.
    Data Source: The logs for May 2024 stored in a GZipped Apache log file containing 258,074 rows.
    The challenge is further complicated by the nature of the log file:

    The logs are recorded in the GMT-0500 timezone.
    The file format is non-standard in that fields are separated by spaces, with most fields quoted by double quotes, except the Time field.
    Some lines have minor formatting issues (41 rows have unique quoting due to how quotes are escaped).
    Your Task
    As a data analyst, you are tasked with determining how many successful GET requests for pages under telugu were made on Monday between 11 and 20 during May 2024. This metric will help:

    Scale Resources: Ensure that servers can handle the peak load during these critical hours.
    Content Planning: Determine the popularity of regional content to decide on future content investments.
    Marketing Insights: Tailor promotional strategies for peak usage times.
    This GZipped Apache log file (61MB) has 258,074 rows. Each row is an Apache web log entry for the site s-anand.net in May 2024.

    Each row has these fields:

    IP: The IP address of the visitor
    Remote logname: The remote logname of the visitor. Typically "-"
    Remote user: The remote user of the visitor. Typically "-"
    Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Not that this is not quoted and you need to handle this.
    Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1
    Status: The HTTP status code. If 200 <= Status < 300 it is a successful request
    Size: The size of the response in bytes. E.g. 1234
    Referer: The referer URL. E.g. https://s-anand.net/
    User agent: The browser used. This will contain spaces and might have escaped quotes.
    Vhost: The virtual host. E.g. s-anand.net
    Server: The IP address of the server.
    The fields are separated by spaces and quoted by double quotes ("). Unlike CSV files, quoted fields are escaped via \" and not "". (This impacts 41 rows.)

    All data is in the GMT-0500 timezone and the questions are based in this same timezone.

    By determining the number of successful GET requests under the defined conditions, we'll be able to:

    Optimize Infrastructure: Scale server resources effectively during peak traffic times, reducing downtime and improving user experience.
    Strategize Content Delivery: Identify popular content segments and adjust digital content strategies to better serve the audience.
    Improve Marketing Efforts: Focus marketing initiatives on peak usage windows to maximize engagement and conversion.
    What is the number of successful GET requests for pages under /telugu/ from 11:00 until before 20:00 on Mondays?""",
    """Bandwidth Analysis for Regional Content
    s-anand.net is a personal website that had region-specific music content. One of the site's key sections is kannada, which hosts music files and is especially popular among the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server load, and content engagement.

    By analyzing the server’s Apache log file, the author can identify heavy users and take measures to manage bandwidth, improve site performance, or even investigate potential abuse.

    Your Task
    This GZipped Apache log file (61MB) has 258,074 rows. Each row is an Apache web log entry for the site s-anand.net in May 2024.

    Each row has these fields:

    IP: The IP address of the visitor
    Remote logname: The remote logname of the visitor. Typically "-"
    Remote user: The remote user of the visitor. Typically "-"
    Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Not that this is not quoted and you need to handle this.
    Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1
    Status: The HTTP status code. If 200 <= Status < 300 it is a successful request
    Size: The size of the response in bytes. E.g. 1234
    Referer: The referer URL. E.g. https://s-anand.net/
    User agent: The browser used. This will contain spaces and might have escaped quotes.
    Vhost: The virtual host. E.g. s-anand.net
    Server: The IP address of the server.
    The fields are separated by spaces and quoted by double quotes ("). Unlike CSV files, quoted fields are escaped via \" and not "". (This impacts 41 rows.)

    All data is in the GMT-0500 timezone and the questions are based in this same timezone.

    Filter the Log Entries: Extract only the requests where the URL starts with /kannada/. Include only those requests made on the specified 2024-05-08.
    Aggregate Data by IP: Sum the "Size" field for each unique IP address from the filtered entries.
    Identify the Top Data Consumer: Determine the IP address that has the highest total downloaded bytes. Reports the total number of bytes that this IP address downloaded.
    Across all requests under kannada/ on 2024-05-08, how many bytes did the top IP address (by volume of downloads) download?""",
    """Sales Analytics at GlobalRetail Insights
    GlobalRetail Insights is a market research and analytics firm specializing in providing data-driven insights for multinational retail companies. Their clients rely on accurate, detailed sales reports to make strategic decisions regarding product placement, inventory management, and marketing campaigns. However, the quality of these insights depends on the reliability of the underlying sales data.

    One major challenge GlobalRetail faces is the inconsistent recording of city names in sales data. Due to human error and regional differences, city names can be mis-spelt (e.g., "Tokio" instead of "Tokyo"). This inconsistency complicates the process of aggregating sales data by city, which is crucial for identifying regional trends and opportunities.

    GlobalRetail Insights recently received a dataset named  from one of its large retail clients. The dataset consists of 2,500 sales entries, each containing the following fields:

    city: The city where the sale was made. Note that city names may be mis-spelt phonetically (e.g., "Tokio" instead of "Tokyo").
    product: The product sold. This field is consistently spelled.
    sales: The number of units sold.
    The client's goal is to evaluate the performance of a specific product across various regions. However, due to the mis-spelled city names, directly aggregating sales by city would lead to fragmented and misleading insights.

    Your Task
    As a data analyst at GlobalRetail Insights, you are tasked with extracting meaningful insights from this dataset. Specifically, you need to:

    Group Mis-spelt City Names: Use phonetic clustering algorithms to group together entries that refer to the same city despite variations in spelling. For instance, cluster "Tokyo" and "Tokio" as one.
    Filter Sales Entries: Select all entries where:
    The product sold is Fish.
    The number of units sold is at least 96.
    Aggregate Sales by City: After clustering city names, group the filtered sales entries by city and calculate the total units sold for each city.
    By performing this analysis, GlobalRetail Insights will be able to:

    Improve Data Accuracy: Correct mis-spellings and inconsistencies in the dataset, leading to more reliable insights.
    Target Marketing Efforts: Identify high-performing regions for the specific product, enabling targeted promotional strategies.
    Optimize Inventory Management: Ensure that inventory allocations reflect the true demand in each region, reducing wastage and stockouts.
    Drive Strategic Decision-Making: Provide actionable intelligence to clients that supports strategic planning and competitive advantage in the market.
    How many units of Fish were sold in Dhaka on transactions with at least 96 units?""",
    """Case Study: Recovering Sales Data for ReceiptRevive Analytics
    ReceiptRevive Analytics is a data recovery and business intelligence firm specializing in processing legacy sales data from paper receipts. Many of the client companies have archives of receipts from past years, which have been digitized using OCR (Optical Character Recognition) techniques. However, due to the condition of some receipts (e.g., torn, faded, or partially damaged), the OCR process sometimes produces incomplete JSON data. These imperfections can lead to truncated fields or missing values, which complicates the process of data aggregation and analysis.

    One of ReceiptRevive’s major clients, RetailFlow Inc., operates numerous brick-and-mortar stores and has an extensive archive of old receipts. RetailFlow Inc. needs to recover total sales information from a subset of these digitized receipts to analyze historical sales performance. The provided JSON data contains 100 rows, with each row representing a sales entry. Each entry is expected to include four keys:

    city: The city where the sale was made.
    product: The product that was sold.
    sales: The number of units sold (or sales revenue).
    id: A unique identifier for the receipt.
    Due to damage to some receipts during the digitization process, the JSON entries are truncated at the end, and the id field is missing. Despite this, RetailFlow Inc. is primarily interested in the aggregate sales value.

    Your Task
    As a data recovery analyst at ReceiptRevive Analytics, your task is to develop a program that will:

    Parse the Sales Data:
    Read the provided JSON file containing 100 rows of sales data. Despite the truncated data (specifically the missing id), you must accurately extract the sales figures from each row.
    Data Validation and Cleanup:
    Ensure that the data is properly handled even if some fields are incomplete. Since the id is missing for some entries, your focus will be solely on the sales values.
    Calculate Total Sales:
    Sum the sales values across all 100 rows to provide a single aggregate figure that represents the total sales recorded.
    By successfully recovering and aggregating the sales data, ReceiptRevive Analytics will enable RetailFlow Inc. to:

    Reconstruct Historical Sales Data: Gain insights into past sales performance even when original receipts are damaged.
    Inform Business Decisions: Use the recovered data to understand sales trends, adjust inventory, and plan future promotions.
    Enhance Data Recovery Processes: Improve methods for handling imperfect OCR data, reducing future data loss and increasing data accuracy.
    Build Client Trust: Demonstrate the ability to extract valuable insights from challenging datasets, thereby reinforcing client confidence in ReceiptRevive's services.
    Download the data from 

    What is the total sales value?""",
    """Log Analysis for DataSure Technologies
    DataSure Technologies is a leading provider of IT infrastructure and software solutions, known for its robust systems and proactive maintenance practices. As part of their service offerings, DataSure collects extensive logs from thousands of servers and applications worldwide. These logs, stored in JSON format, are rich with information about system performance, error events, and user interactions. However, the logs are complex and deeply nested, which can make it challenging to quickly identify recurring issues or anomalous behavior.

    Recently, DataSure's operations team observed an increase in system alerts and minor anomalies reported by their monitoring tools. To diagnose these issues more effectively, the team needs to perform a detailed analysis of the log files. One critical step is to count how often a specific key (e.g., "errorCode", "criticalFlag", or any other operational parameter represented by Q) appears in the log entries.

    Key considerations include:

    Complex Structure: The log files are large and nested, with multiple levels of objects and arrays. The target key may appear at various depths.
    Key vs. Value: The key may also appear as a value within the logs, but only occurrences where it is a key should be counted.
    Operational Impact: Identifying the frequency of this key can help pinpoint common issues, guide system improvements, and inform maintenance strategies.
    Your Task
    As a data analyst at DataSure Technologies, you have been tasked with developing a script that processes a large JSON log file and counts the number of times a specific key, represented by the placeholder Q, appears in the JSON structure. Your solution must:

    Parse the Large, Nested JSON: Efficiently traverse the JSON structure regardless of its complexity.
    Count Key Occurrences: Increment a count only when Q is used as a key in the JSON object (ignoring occurrences of Q as a value).
    Return the Count: Output the total number of occurrences, which will be used by the operations team to assess the prevalence of particular system events or errors.
    By accurately counting the occurrences of a specific key in the log files, DataSure Technologies can:

    Diagnose Issues: Quickly determine the frequency of error events or specific system flags that may indicate recurring problems.
    Prioritize Maintenance: Focus resources on addressing the most frequent issues as identified by the key count.
    Enhance Monitoring: Improve automated monitoring systems by correlating key occurrence data with system performance metrics.
    Inform Decision-Making: Provide data-driven insights that support strategic planning for system upgrades and operational improvements.
    Download the data from 

    How many times does Q appear as a key?""",
    """Identifying High-Impact Social Media Posts for EngageMetrics
    EngageMetrics is a digital marketing analytics firm that specializes in tracking and analyzing social media engagement. Their clients, ranging from major brands to local businesses, rely on data-driven insights to optimize content strategy, measure campaign performance, and identify posts that drive significant user interaction.

    Social media platforms generate vast amounts of user-generated content, including posts, comments, likes, and ratings. One key metric that EngageMetrics uses is the “usefulness” of comments on posts. A comment rated highly on usefulness is a strong indicator that a post is engaging and valuable to its audience.

    However, the raw data is complex and stored in a DuckDB table called social_media, which is generated by a simulated dataset. Each row in the table represents a post with the following fields:

    post_id: A unique identifier for the post.
    username: The user who created the post.
    timestamp: The time when the post was made.
    comments: A JSON array containing comments. Each comment includes:
    commenter: The user who commented.
    text: The comment text.
    stars: An object with two properties, funny and useful, representing the rating stars for that comment.
    Due to the dynamic nature of social media, EngageMetrics wants to focus on the most recent posts and, within those, identify posts where at least one comment has received a high number of useful stars. This allows the firm to spotlight content that is not only fresh but also resonating well with the audience.

    Your Task
    Your task as a data analyst at EngageMetrics is to write a query that performs the following:

    Filter Posts by Date: Consider only posts with a timestamp greater than or equal to a specified minimum time (2024-12-26T13:49:31.009Z), ensuring that the analysis focuses on recent posts.
    Evaluate Comment Quality: From these recent posts, identify posts where at least one comment has received more than a given number of useful stars (5). This criterion filters out posts with low or mediocre engagement.
    Extract and Sort Post IDs: Finally, extract all the post_id values of the posts that meet these criteria and sort them in ascending order.
    By accurately extracting these high-impact post IDs, EngageMetrics can:

    Enhance Reporting: Provide clients with focused insights on posts that are currently engaging audiences effectively.
    Target Content Strategy: Help marketing teams identify trending content themes that generate high-quality user engagement.
    Optimize Resource Allocation: Enable better prioritization for content promotion and further in-depth analysis of high-performing posts.
    Write a DuckDB SQL query to find all posts IDs after 2024-12-26T13:49:31.009Z with at least 1 comment with 5 useful stars, sorted. The result should be a table with a single column called post_id, and the relevant post IDs should be sorted in ascending order.
    Check the console for the result of your query.""",
    """Enhancing Accessibility and Content Analysis for Mystery Audiobooks
    Mystery Tales Publishing is an independent publisher specializing in mystery and suspense audiobooks. To broaden their audience and improve accessibility, they have been uploading narrated versions of their stories to YouTube. In addition to reaching visually impaired users, they want to leverage transcripts for content summarization, search indexing, and social media promotion.

    The company has identified that certain segments of their mystery story audiobooks generate the most engagement. However, transcribing entire videos can be time-consuming and may include irrelevant content. Therefore, they have decided to focus on transcribing only the most compelling segments. For instance, a particular segment—from 259.7 to 351.8—is known to captivate listeners with a twist in the plot. An accurate transcript of this segment will:

    Enhance accessibility by providing a text alternative for hearing-impaired users.
    Improve search engine optimization (SEO) through indexed keywords.
    Support content analysis and summarization for promotional purposes.
    As part of a pilot project, you are tasked with transcribing the YouTube video segment of a mystery story audiobook. You are provided with a sample video that features a narrated mystery story. Your focus will be on the segment starting at 259.7 and ending at 351.8.

    Your transcription should:

    Accurately capture all spoken dialogue and descriptive narration.
    Include appropriate punctuation and paragraph breaks to reflect natural speech.
    Exclude any extraneous noise or background commentary not relevant to the narrative.
    Your Task
    Access the Video: Use the provided YouTube link to access the mystery story audiobook.
    Convert to Audio: Extract the audio for the segment between 259.7 and 351.8.
    Transcribe the Segment: Utilize automated speech-to-text tools as needed.
    By producing an accurate transcript of this key segment, Mystery Tales Publishing will be able to:

    Boost Accessibility: Provide high-quality captions and text alternatives for hearing-impaired users.
    Enhance SEO: Improve the discoverability of their content through better keyword indexing.
    Drive Engagement: Use the transcript for social media snippets, summaries, and promotional materials.
    Enable Content Analysis: Facilitate further analysis such as sentiment analysis, topic modeling, and reader comprehension studies.
    What is the text of the transcript of this Mystery Story Audiobook between 259.7 and 351.8 seconds?""",
    """Image Reconstruction for Forensic Analysis
    PixelGuard Solutions is a digital forensics firm specializing in the recovery and analysis of visual evidence for law enforcement and corporate investigations. One of their recurring challenges involves reconstructing damaged or deliberately scrambled images to reveal hidden details critical to solving cases.

    In a recent investigation, law enforcement received an anonymous tip involving a scrambled image that appeared to contain sensitive information. The image had been deliberately cut into 25 (5x5) pieces and rearranged to obfuscate its content. Recovering the original image was essential for uncovering evidence related to the case.

    PixelGuard's forensic team extracted the scrambled pieces and obtained a mapping file that specifies the transformation from the original (row, col) positions to the new positions. However, the team now needs to reassemble the image according to this mapping to restore its original appearance.

    Your Task
    As a digital forensics analyst at PixelGuard Solutions, your task is to reconstruct the original image from its scrambled pieces. You are provided with:

    The 25 individual image pieces (put together as a single image).
    A mapping file detailing the original (row, col) position for each piece and its current (row, col) location.
    Your reconstructed image will be critical evidence in the investigation. Once assembled, the image must be uploaded to the secure case management system for further analysis by the investigative team.

    Understand the Mapping: Review the provided mapping file that shows how each piece's original coordinates (row, col) relate to its current scrambled position.
    Reassemble the Image: Using the mapping, reassemble the 5x5 grid of image pieces to reconstruct the original image. You may use an image processing library (e.g., Python's Pillow, ImageMagick, or a similar tool) to automate the reconstruction process.
    Output the Reconstructed Image: Save the reassembled image in a lossless format (e.g., PNG or WEBP). Upload the reconstructed image to the secure case management system as required by PixelGuard’s workflow.
    By accurately reconstructing the scrambled image, PixelGuard Solutions will:

    Reveal Critical Evidence: Provide investigators with a clear view of the original image, which may contain important details related to the case.
    Enhance Analytical Capabilities: Enable further analysis and digital enhancements that can lead to breakthroughs in the investigation.
    Maintain Chain of Custody: Ensure that the reconstruction process is documented and reliable, supporting the admissibility of the evidence in court.
    Improve Operational Efficiency: Demonstrate the effectiveness of automated image reconstruction techniques in forensic investigations.
    Here is the image. It is a 500x500 pixel image that has been cut into 25 (5x5) pieces:

    Here is the mapping of each piece:

    Original Row	Original Column	Scrambled Row	Scrambled Column
    2	1	0	0
    1	1	0	1
    4	1	0	2
    0	3	0	3
    0	1	0	4
    1	4	1	0
    2	0	1	1
    2	4	1	2
    4	2	1	3
    2	2	1	4
    0	0	2	0
    3	2	2	1
    4	3	2	2
    3	0	2	3
    3	4	2	4
    1	0	3	0
    2	3	3	1
    3	3	3	2
    4	4	3	3
    0	2	3	4
    3	1	4	0
    1	2	4	1
    1	3	4	2
    0	4	4	3
    4	0	4	4
    Upload the reconstructed image by moving the pieces from the scrambled position to the original position:"""
    ]

questions = ga1questions + ga2questions + ga3questions + ga4questions + ga5questions
import numpy as np
import torch

def save_embeddings_npy(embeddings, filename="embeddings.npy"):
    np.save(filename, embeddings)

def load_embeddings_npy(filename="embeddings.npy"):
    return torch.tensor(np.load(filename, allow_pickle=True))

def create_embedding():
    # Compute embeddings for the questions
    question_embeddings = model.encode(questions, convert_to_tensor=True)
    save_embeddings_npy(question_embeddings)
    return question_embeddings

def q_embed(q):
    return model.encode(q, convert_to_tensor=True)

#create_embedding()