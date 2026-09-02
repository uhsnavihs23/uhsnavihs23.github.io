import re

with open('about.html', 'r') as f:
    content = f.read()

ai_tools = """
                    <!-- AI Tools -->
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="ChatGPT">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-6 w-6"><path fill="currentColor" d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.073zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.8956zm16.0993 3.8558L12.5973 8.3829a.0757.0757 0 0 1-.0379-.052V2.7483a4.504 4.504 0 0 1 5.8683 1.637l-.1419.0804-4.783 2.7582a.7948.7948 0 0 0-.3927.6813v6.7369l2.02-1.1686a.071.071 0 0 1 .038-.052v-5.5826a4.504 4.504 0 0 1 5.2536-4.2255zm-1.0264 6.3262l-4.783-2.7582a.7712.7712 0 0 0-.7806 0l-5.8428 3.3685v-2.3324a.0804.0804 0 0 1 .0332-.0615l4.835-2.7913a4.4992 4.4992 0 0 1 6.1408 1.6464V18.0776zm-8.8775-6.8407l-2.02-1.1685a.071.071 0 0 1-.038-.052V4.4338a4.504 4.504 0 0 1 5.2536 4.2255l-.142-.0852-4.783-2.7582a.7948.7948 0 0 0-.3927-.6813v6.7369a.071.071 0 0 1-.038.052l-2.02 1.1686zM12 14.1798l-2.946-1.7011v-3.4022L12 7.3754l2.946 1.7011v3.4022L12 14.1798z"/></svg>
                    </div>
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="GitHub Copilot">
                        <img src="https://cdn.simpleicons.org/githubcopilot/000000" alt="Copilot" class="h-6 w-6 dark:invert">
                    </div>
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="Claude">
                        <img src="https://cdn.simpleicons.org/anthropic/000000" alt="Claude" class="h-6 w-6 dark:invert">
                    </div>
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="Gemini">
                        <img src="https://cdn.simpleicons.org/googlegemini/4285F4" alt="Gemini" class="h-6 w-6">
                    </div>
                    <div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="Perplexity">
                        <img src="https://cdn.simpleicons.org/perplexity/222222" alt="Perplexity" class="h-6 w-6 dark:invert">
                    </div>
"""

# inject AI tools at the end of the flex container for tech stack
content = re.sub(r'(<div class="h-10 w-10 bg-cardBg rounded-xl shadow-sm border border-borderColor flex items-center justify-center hover:scale-110 transition-transform hover:shadow-lg" title="Power BI">.*?</div>)', r'\1' + ai_tools, content, flags=re.DOTALL)

with open('about.html', 'w') as f:
    f.write(content)
