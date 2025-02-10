
from get_content import read_text_from_pdf
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
load_dotenv()

import asyncio


spanish_text=read_text_from_pdf('email_document.pdf')

task="""
   ### Prompt for Shopping Agent – Migros Online Grocery Order

**Objective:**  
Visit [Google Translate](http://translate.google.com/), translate a text from Spanish to English, and write a letter to your colleague in English in docs.goole.com.

**Important:**
- Make sure that you write a letter to your friend in English and explain some challanges in spanish
---

### Step 1: Navigate to the Website
- Open [Google Translate](http://translate.google.com/).

---

### Step 2: Select the Languages
- Select the **source language** as **Spanish**.
- Select the **target language** as **English**.
- Enter the following text in Spanish: "{spanish_text}"
---

### Step 3: Copy the Translated Text
- Navigate to https://docs.google.com/document/u/0/ write my colleague a quick letter with summary at the end and along with it date and time
- Explain him how you are doing and what you are up to.
- Tell him about your plans for the weekend. and use the translated text
---

**Important:** Ensure efficiency and accuracy throughout the process."""

# browser = Browser()

browser = Browser(
	config=BrowserConfig(
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)

agent = Agent(
   task=task,
    llm=ChatOpenAI(model="gpt-4o"),
    browser=browser,
    )

async def main():
    await agent.run()
    input("Press Enter to close the browser...")
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())