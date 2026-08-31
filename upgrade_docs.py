from pathlib import Path
import re

ROOT = Path.cwd()
HTML = ROOT / "index.html"
BACKUP = ROOT / "index.html.before-qntaai-upgrade"

if not HTML.exists():
    raise SystemExit("ERROR: index.html not found.")

text = HTML.read_text(encoding="utf-8")

# ============================================================
# BACKUP
# ============================================================

if not BACKUP.exists():
    BACKUP.write_text(text, encoding="utf-8")
    print("Created backup:", BACKUP.name)
else:
    print("Backup already exists:", BACKUP.name)


# ============================================================
# REMOVE EMOJIS
# ============================================================

emoji_pattern = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "\U00002700-\U000027BF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA70-\U0001FAFF"
    "]+",
    flags=re.UNICODE
)

text = emoji_pattern.sub("", text)

# Remove excessive spaces left behind by emoji removal.
text = re.sub(r"[ \t]{2,}", " ", text)


# ============================================================
# NAME CORRECTIONS
# ============================================================

text = text.replace(
    "Suryansh Singh Bhadoriya",
    "Suryansh Singh Bhadouriya"
)

text = text.replace(
    "Bhadoriya",
    "Bhadouriya"
)


# ============================================================
# UPDATE MODEL SECTION
# ============================================================

# Find <section ... id="models" ...> regardless of whitespace.
model_match = re.search(
    r"<section\b[^>]*\bid=[\"']models[\"'][^>]*>",
    text,
    flags=re.IGNORECASE
)

if not model_match:
    raise SystemExit(
        "ERROR: Models section not found.\n"
        "The HTML does not contain a <section> with id=\"models\"."
    )

model_start = model_match.start()

# Find the next section after the models section.
next_section = text.find(
    "<section",
    model_match.end()
)

if next_section == -1:
    raise SystemExit(
        "ERROR: End of Models section not found."
    )


models_section = r'''<section
    class="section"
    id="models"
>

    <div class="section-header">

        <p class="section-label">
            Model Selection
        </p>

        <h2>
            Multiple AI models
        </h2>

        <p class="section-intro">
            QntaAI is not tied to a single AI model.
            Users can select from the available models
            through the model selector. This provides
            flexibility when choosing an AI experience
            for different tasks.
        </p>

    </div>

    <div class="table-container">

        <table>

            <thead>

                <tr>
                    <th>Model</th>
                    <th>Provider</th>
                    <th>Model ID</th>
                </tr>

            </thead>

            <tbody>

                <tr>
                    <td>Auto Free</td>
                    <td>OpenRouter</td>
                    <td><code>openrouter/free</code></td>
                </tr>

                <tr>
                    <td>Ling 3.0 Flash Fin</td>
                    <td>InclusionAI</td>
                    <td><code>inclusionai/ling-3.0-flash-fin:free</code></td>
                </tr>

                <tr>
                    <td>Dots 3 Note Preview</td>
                    <td>Dots Studio</td>
                    <td><code>dots-studio/dots-3-note-preview:free</code></td>
                </tr>

                <tr>
                    <td>LFM 2.5 2.6B</td>
                    <td>Liquid</td>
                    <td><code>liquid/lfm-2.5-2.6b:free</code></td>
                </tr>

                <tr>
                    <td>Nemotron 3.5 Lightning</td>
                    <td>NVIDIA</td>
                    <td><code>nvidia/nemotron-3.5-lightning:free</code></td>
                </tr>

                <tr>
                    <td>Inkling Small</td>
                    <td>Thinking Machines</td>
                    <td><code>thinkingmachines/inkling-small:free</code></td>
                </tr>

                <tr>
                    <td>Laguna S 2.1</td>
                    <td>Poolside</td>
                    <td><code>poolside/laguna-s-2.1:free</code></td>
                </tr>

                <tr>
                    <td>Inkling</td>
                    <td>Thinking Machines</td>
                    <td><code>thinkingmachines/inkling:free</code></td>
                </tr>

                <tr>
                    <td>Laguna XS 2.1</td>
                    <td>Poolside</td>
                    <td><code>poolside/laguna-xs-2.1:free</code></td>
                </tr>

                <tr>
                    <td>North Mini Code</td>
                    <td>Cohere</td>
                    <td><code>cohere/north-mini-code:free</code></td>
                </tr>

                <tr>
                    <td>GLM 5.2</td>
                    <td>Z.ai</td>
                    <td><code>z-ai/glm-5.2:free</code></td>
                </tr>

                <tr>
                    <td>Nemotron 3 Ultra</td>
                    <td>NVIDIA</td>
                    <td><code>nvidia/nemotron-3-ultra-550b-a55b:free</code></td>
                </tr>

                <tr>
                    <td>MiniMax M3</td>
                    <td>MiniMax</td>
                    <td><code>minimax/minimax-m3:free</code></td>
                </tr>

                <tr>
                    <td>Nemotron 3 Nano Omni</td>
                    <td>NVIDIA</td>
                    <td><code>nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free</code></td>
                </tr>

                <tr>
                    <td>Gemma 4 26B</td>
                    <td>Google</td>
                    <td><code>google/gemma-4-26b-a4b-it:free</code></td>
                </tr>

                <tr>
                    <td>Gemma 4 31B</td>
                    <td>Google</td>
                    <td><code>google/gemma-4-31b-it:free</code></td>
                </tr>

                <tr>
                    <td>MiniMax M2.7</td>
                    <td>MiniMax</td>
                    <td><code>minimax/minimax-m2.7:free</code></td>
                </tr>

                <tr>
                    <td>Nemotron 3 Super</td>
                    <td>NVIDIA</td>
                    <td><code>nvidia/nemotron-3-super-120b-a12b:free</code></td>
                </tr>

            </tbody>

        </table>

    </div>

    <div class="card-grid model-summary-grid">

        <div class="card">

            <h3>
                Model independence
            </h3>

            <p>
                QntaAI can route requests to different
                supported models instead of relying on
                a single AI model.
            </p>

        </div>

        <div class="card">

            <h3>
                User choice
            </h3>

            <p>
                The model selector allows users to choose
                an available model according to the task
                they are working on.
            </p>

        </div>

        <div class="card">

            <h3>
                Unified interface
            </h3>

            <p>
                Different AI models are presented through
                the same QntaAI interface and backend.
            </p>

        </div>

    </div>

</section>


'''

text = (
    text[:model_start]
    + models_section
    + text[next_section:]
)


# ============================================================
# UPDATE PROJECT STRUCTURE
# ============================================================

old_structure = r'''<pre>
QntaAI
│
├── Frontend
│   ├── Interface
│   └── Chat UI
│
├── Backend
│   ├── Application Server
│   ├── Chat Handling
│   └── Search Logic
│
├── AI
│   ├── GPT
│   ├── Gemini
│   └── Grok
│
├── Search
│   ├── Quick
│   ├── Search
│   └── Research
│
└── Documentation
    └── QntaAI Official Documentation
</pre>'''

new_structure = r'''<pre>
QntaAI
│
├── Frontend
│   ├── Interface
│   ├── Chat UI
│   └── Model Selector
│
├── Backend
│   ├── Application Server
│   ├── Chat Handling
│   ├── Model Validation
│   └── Search Logic
│
├── AI
│   ├── OpenRouter
│   ├── Model Routing
│   └── Multiple Supported Models
│
├── Search
│   ├── Quick
│   ├── Search
│   └── Research
│
├── Storage
│   └── Conversation Data
│
└── Documentation
    └── QntaAI Official Documentation
</pre>'''

if old_structure in text:
    text = text.replace(old_structure, new_structure, 1)


# ============================================================
# UPDATE FAQ
# ============================================================

old_faq = '''        <p>
            QntaAI currently provides model choices
            including GPT, Gemini, and Grok.
        </p>'''

new_faq = '''        <p>
            QntaAI provides a multi-model selector with
            multiple supported models available through
            the backend. The available model catalog can
            change as model availability changes.
        </p>'''

text = text.replace(old_faq, new_faq, 1)


# ============================================================
# ADD CURRENT CAPABILITIES
# ============================================================

architecture_anchor = '''<!-- =========================================
     ARCHITECTURE
     ========================================= -->'''

capabilities = r'''<!-- =========================================
     CURRENT CAPABILITIES
     ========================================= -->

<section class="section">

    <div class="section-header">

        <p class="section-label">
            Capabilities
        </p>

        <h2>
            Current QntaAI capabilities
        </h2>

        <p class="section-intro">
            The current QntaAI application combines
            conversational AI, model selection, search
            modes, conversation history, and a responsive
            web interface.
        </p>

    </div>

    <div class="card-grid">

        <div class="card">

            <h3>
                Multi-model AI
            </h3>

            <p>
                Select from multiple supported AI models
                instead of being permanently tied to a
                single model.
            </p>

        </div>

        <div class="card">

            <h3>
                Conversation history
            </h3>

            <p>
                Conversations can be stored and revisited
                through the QntaAI chat interface.
            </p>

        </div>

        <div class="card">

            <h3>
                Search modes
            </h3>

            <p>
                Quick, Search, and Research experiences
                provide different approaches to answering
                user questions.
            </p>

        </div>

        <div class="card">

            <h3>
                File support
            </h3>

            <p>
                The interface can support file attachments
                where enabled by the application.
            </p>

        </div>

        <div class="card">

            <h3>
                Responsive interface
            </h3>

            <p>
                The web interface is designed to adapt
                across desktop and mobile screen sizes.
            </p>

        </div>

        <div class="card">

            <h3>
                Web deployment
            </h3>

            <p>
                QntaAI operates as a web application with
                its frontend and backend working together.
            </p>

        </div>

    </div>

</section>


'''

if architecture_anchor in text and "CURRENT CAPABILITIES" not in text:
    text = text.replace(
        architecture_anchor,
        capabilities + architecture_anchor,
        1
    )


# ============================================================
# ADD PROFESSIONAL CSS
# ============================================================

css_anchor = '''        /* =========================================
           ARCHITECTURE
           ========================================= */'''

extra_css = r'''        /* =========================================
           DOCUMENTATION ENHANCEMENTS
           ========================================= */

        code {
            font-family:
                Consolas,
                "Courier New",
                monospace;

            font-size: 0.9em;

            color: #c5c5ff;

            background: #11111a;

            padding: 3px 7px;

            border-radius: 5px;

            border: 1px solid #242432;
        }

        .model-summary-grid {
            margin-top: 25px;
        }

        .table-container {
            scrollbar-width: thin;
        }

        th {
            white-space: nowrap;
        }

        td code {
            white-space: nowrap;
        }

        .back-to-top {
            position: fixed;

            right: 20px;
            bottom: 20px;

            width: 44px;
            height: 44px;

            display: flex;

            align-items: center;
            justify-content: center;

            text-decoration: none;

            background: #0c0c12;

            border: 1px solid #30303a;

            border-radius: 50%;

            color: #ffffff;

            font-size: 18px;

            opacity: 0.85;

            transition: 0.25s ease;

            z-index: 900;
        }

        .back-to-top:hover {
            transform: translateY(-3px);

            border-color: #5555ff;

            box-shadow: 0 0 20px #5555ff33;

            opacity: 1;
        }

        @media (max-width: 600px) {

            .table-container {
                border-radius: 10px;
            }

            th,
            td {
                padding: 13px;
            }

            td code {
                font-size: 11px;
            }

            .back-to-top {
                right: 14px;
                bottom: 14px;
            }
        }


'''

if css_anchor in text and "DOCUMENTATION ENHANCEMENTS" not in text:
    text = text.replace(
        css_anchor,
        extra_css + css_anchor,
        1
    )


# ============================================================
# ADD BACK-TO-TOP BUTTON
# ============================================================

body_end = '''</body>
</html>'''

back_to_top = r'''<a
    class="back-to-top"
    href="#top"
    aria-label="Back to top"
    title="Back to top"
>
    ↑
</a>

'''

if 'class="back-to-top"' not in text:
    text = text.replace(
        body_end,
        back_to_top + body_end,
        1
    )


# ============================================================
# ADD TOP ANCHOR
# ============================================================

if '<body id="top">' not in text:
    text = text.replace(
        "<body>",
        '<body id="top">',
        1
    )


# ============================================================
# FINAL CLEANUP
# ============================================================

text = re.sub(
    r"\n{4,}",
    "\n\n\n",
    text
)

HTML.write_text(text, encoding="utf-8")


# ============================================================
# VERIFY
# ============================================================

final_text = HTML.read_text(encoding="utf-8")

checks = {
    "Models section": bool(
        re.search(
            r'<section\b[^>]*\bid=["\']models["\']',
            final_text,
            re.IGNORECASE
        )
    ),
    "Correct surname": "Suryansh Singh Bhadouriya" in final_text,
    "Capabilities section": "CURRENT CAPABILITIES" in final_text,
    "Back-to-top": 'class="back-to-top"' in final_text,
    "Model selector wording": "Multiple AI models" in final_text,
}

print()
print("==========================================")
print(" QntaAI DOCUMENTATION UPGRADE COMPLETE")
print("==========================================")
print()
print("Updated:")
print("  index.html")
print()
print("Changes:")
print("  - Removed documentation emojis")
print("  - Fixed surname: Bhadouriya")
print("  - Updated multi-model documentation")
print("  - Added model IDs and providers")
print("  - Updated project architecture")
print("  - Updated model-selection FAQ")
print("  - Added current capabilities section")
print("  - Added model summary cards")
print("  - Added code styling")
print("  - Added back-to-top control")
print("  - Improved mobile model-table behavior")
print()
print("Verification:")

for name, passed in checks.items():
    print("  " + ("[OK] " if passed else "[FAIL] ") + name)

print()
print("Backup:")
print("  index.html.before-qntaai-upgrade")
print()
