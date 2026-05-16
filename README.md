# This is a learning project for backend frontend integration.
### Goal is to create a ai-like website which talks to ollama and can switch models so basically local and free chatgpt/claude whichever we can access via ollama.

*Current Progress:*
- Learned fastapi , endpoints, like get post etc, used responses to get response from local ollama at 11434 and format that in json and return it, so flow is frontend req->backend sends message to generate end point of ollama -> get back response -> return to frontend
- Use of cors (by default intra port communication is blocked by web browser this allows it)
- get post delete patch etc are just methods that can be called via a http request
- frontend uses axios (simpler to write than fetch) to get response from the post method which i have defined in backend
- very simple single generate app made, no context or chat feature, single message and single response system