**Comprehensive Context for AI Chatbot Development Conversation:**

**Goal:** To develop an AI-powered Slackbot for SkillUp Life, a volunteer management platform. The initial focus (MVP) is on automating the collection and summarization of daily updates from product team members in a designated Slack channel (`#daily-updates`). Future phases will include broader question answering capabilities, integration with Google Sheets and GitHub, and potentially a fully offline deployment.

**Key Requirements and Features (Initial and Future):**

* **Daily Update Monitoring & Summarization (MVP):**
    * Monitor the `#daily-updates` Slack channel for new messages.
    * Identify updates from specific product team members (initially by manual user ID, later potentially more dynamic).
    * Extract key information from daily update messages (initially based on a defined format).
    * Use an LLM (`gpt-4o-mini` initially) with a specific prompt (provided later in the conversation) to generate a concise, high-level summary of the extracted updates.
    * Post the generated summary to a designated Slack channel at a specific time.
    * Store raw and summarized daily updates in a Supabase database (`daily_updates` table).
    * Generate and store embeddings of the daily updates in the `documents` table in Supabase using the `pgvector` extension.

* **Future Considerations:**
    * Knowing who is on specific Slack channels for different product teams.
    * Selective information retrieval from a general channel for specific team members.
    * Permission-based actions and reminders (with admin approval workflows).
    * Direct messaging capabilities with users for personal tasks.
    * Integration with a separate calendar bot.
    * Team membership verification.
    * Tracking what team members said they would do.
    * Google Sheets integration (CRUD operations).
    * Handling "no update" scenarios gracefully.
    * Integration with GitHub projects.
    * Potential future integration with Telegram and locally hosted LLMs (Ollama).

**Technology Stack (Current and Planned):**

* **Automation Engine:** N8N (Workflow Automation Engine) - for low-code workflow creation and integration.
* **Database and Vector DB:** Supabase (free tier initially) with the `pgvector` extension for vector storage and similarity searches.
* **Embedding Model:** OpenAI `text-embedding-ada-002` - for generating text embeddings.
* **LLM for Summarization:** OpenAI `gpt-4o-mini` (initial focus due to cost-effectiveness).
* **Slack Integration:** Slack API - for interacting with the Slack workspace.
* **Hosting:** N8N Cloud (free tier initially) and Supabase Cloud (free tier).
* **Version Control:** GitHub - for managing N8N workflow JSON exports and other project documents (using VSCode for management).

**Key Decisions and Considerations:**

* **Start Simple (MVP):** Focus on the daily update monitoring and summarization as the initial Minimum Viable Product.
* **Modular Design:** Build the bot in a modular way to easily add new features in the future.
* **Cost-Consciousness:** Utilize free tiers and cost-effective LLM options initially.
* **Privacy (Future Goal):** Work towards a fully offline product using locally hosted LLMs (Ollama) in the long term.
* **Supabase as Central Platform:** Leverage Supabase for both the relational database (for structured data) and the vector database (using `pgvector`).
* **N8N Workflow Management:** Manage N8N workflows within its UI and use GitHub for backup and version control of exported JSON files.
* **Utilizing External Resources:** We identified a relevant video and GitHub repository ([https://github.com/coleam00/ai-agents-masterclass/tree/main/supabase-n8n-rag-agent](https://github.com/coleam00/ai-agents-masterclass/tree/main/supabase-n8n-rag-agent)) demonstrating RAG with Supabase and N8N, which will be a valuable reference.

**Next Steps (Based on the Conversation):**

1.  Set up a Supabase project and enable the `pgvector` extension.
2.  Install and familiarize yourself with N8N.
3.  Create a Slack App and obtain the necessary API credentials.
4.  Import and adapt the RAG workflow from the provided GitHub repository into N8N to handle daily updates and summarization.
5.  Create Supabase tables (`daily_updates`, `documents`).
6.  Build the N8N workflow to:
    * Listen for Slack messages.
    * Identify relevant updates.
    * Extract information.
    * Use `gpt-4o-mini` and the provided prompt for summarization.
    * Store raw and summarized updates in Supabase.
    * Generate and store embeddings of the updates in Supabase using `pgvector`.
    * Post the summary to Slack.
7.  Set up a GitHub repository for project files and N8N workflow backups.

**Provided Prompt for Daily Updates:** 
Prompt for Daily Updates
Absolutely! Here’s a **detailed and structured prompt** that will ensure you consistently get a **concise, comprehensive, and high-level summary** based on the daily updates from the product team. This prompt will help maintain strategic clarity while ensuring accuracy.

---

### **Prompt for Generating High-Level Status Summaries from Daily Updates**  

**Context:**  
Each day, the product team provides individual updates on their tasks, blockers, and accomplishments. The goal is to synthesize these updates into a **concise, high-level summary** that reflects the current state of progress across key modules while maintaining a strategic overview.  

**Instructions:**  
1. **Extract Relevant Updates**  
   - Identify updates related to **Company Account Management (Module 1)** and **Volunteer Account Management (Module 2)**.  
   - Ignore updates that do not contribute directly to the sprint tracking (e.g., onboarding, general meetings, or unrelated discussions).  

2. **Structure the Summary Using the Following Format:**  
   - **Module 1 - Company Account Management**  
     - **Company Login - [Status]**  
       - **Primary blockers:** [Summarized blockers]  
       - [Concise bullet points summarizing progress]  
     - **Company Registration - [Status]**  
       - **Primary blockers:** [Summarized blockers]  
       - [Concise bullet points summarizing progress]  
     - *(Repeat for all sub-items in Module 1 in the predefined order)*  
   - **Module 2 - Volunteer Account Management**  
     - **Volunteer Login - [Status]**  
       - **Primary blockers:** [Summarized blockers]  
       - [Concise bullet points summarizing progress]  
     - *(Repeat for all sub-items in Module 2 in the predefined order)*  

3. **Ensure Strategic Clarity**  
   - Keep the summary **fact-based**, strictly reflecting the updates provided.  
   - Avoid assumptions—only include blockers and progress explicitly mentioned in the daily updates.  
   - Maintain a **high-level perspective** by focusing on **overall progress** rather than individual task details.  

4. **Highlight Pending Items Separately**  
   - If any critical blockers or pending confirmations arise, list them under **Pending Items** at the end of the summary.  
   - Example:  
     - **Subscription Keys** – Awaiting confirmation from [Team Member].  
     - **Volunteer Profiles** – Expected completion tomorrow per [Team Member].  

5. **Use Clear and Concise Language**  
   - Keep sentences **short and actionable**.  
   - Use **neutral phrasing** to maintain a professional tone.  
   - Example: Instead of *"Some issues might still exist in mobile registration,"* say *"Mobile registration validation is ongoing."*  

---

### **Example Output Using This Prompt**  

#### **Module 1 - Company Account Management**  

**Company Login - In Progress**  
**Primary blockers:** Profile completion validation, mobile registration barriers.  
- Registration flow requires final validation—users cannot proceed without completing profiles.  
- Mobile registration process remains inconsistent—users face confirmation email issues.  

**Company Subscription - In Progress**  
**Primary blockers:** Stripe payment integration pending validation.  
- Subscription functionality is integrated but requires testing.  
- Payment success handling is in development.  

#### **Module 2 - Volunteer Account Management**  

**Volunteer Profiles - In Progress**  
**Primary blockers:** UI refinements required before completion.  
- Expected completion tomorrow per Khaled.  
- Mobile profile display updates are ongoing.  

**Apply for Opportunities - In Progress**  
**Primary blockers:** Applicant display functionality pending implementation.  
- Specification for "My Opportunities" is complete, but functionality remains incomplete.  

#### **Pending Items:**  
- **Subscription Keys** – Confirmed as sorted yesterday.  
- **New Team Members** – Awaiting update from Grace.  

---

### **How to Use This Prompt**  
Whenever you receive **daily updates from the product team**, simply apply this structured approach to extract relevant details and generate a **concise, high-level summary**. This will ensure consistency, clarity, and strategic alignment in your sprint tracking.


Updated Prompt for Generating High-Level Status Summaries
Instructions:

Extract Relevant Updates

Identify updates related to Company Account Management (Module 1) and Volunteer Account Management (Module 2).

Categorize updates under Design, Dev, and QA where applicable.

Structure the Summary Using the Following Format:

Module 1 - Company Account Management

Company Login - [Status]

Design: [Design-related updates]

Dev: [Development-related updates]

QA: [Testing-related updates]

(Repeat for all sub-items in Module 1 in the predefined order)

Module 2 - Volunteer Account Management

Volunteer Login - [Status]

Design: [Design-related updates]

Dev: [Development-related updates]

QA: [Testing-related updates]

(Repeat for all sub-items in Module 2 in the predefined order)

Ensure Strategic Clarity

Keep the summary fact-based, strictly reflecting the updates provided.

Avoid assumptions—only include blockers and progress explicitly mentioned in the daily updates.

Maintain a high-level perspective by focusing on overall progress rather than individual task details.

Final Thoughts
This small but impactful change will make the report more useful for both Manoj and Cathrine, ensuring that design work isn’t mistakenly marked as “in progress” when it’s actually done.