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
    print("Backup created:", BACKUP.name)
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
    "\U0001F900-\U0001F9FF"
    "]+",
    flags=re.UNICODE
)

text = emoji_pattern.sub("", text)


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
# UPDATE MODELS SECTION
# ============================================================

models_start_match = re.search(
    r'<section\b[^>]*\bid=["\']models["\'][^>]*>',
    text,
    flags=re.IGNORECASE
)

if not models_start_match:
    raise SystemExit("ERROR: Models section not found.")

models_start = models_start_match.start()

next_section_match = re.search(
    r'<section\b',
    text[models_start_match.end():],
    flags=re.IGNORECASE
)

if not next_section_match:
    raise SystemExit("ERROR: End of Models section not found.")

models_end = (
    models_start_match.end()
    + next_section_match.start()
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
            through the model selector. This allows
            different models to be used for different
            tasks and response styles.
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
                    <td>Auto (Free)</td>
                    <td>OpenRouter</td>
                    <td><code>openrouter/free</code></td>
                </tr>

                <tr>
                    <td>Ling 3.0 Flash Fin</td>
                    <td>InclusionAI</td>
                    <td><code>inclusionai/ling-3.0-flash-fin:free</code></td>
                </tr>

                <tr>
                    <td>Dots3 Note Preview</td>
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
                one model provider.
            </p>

        </div>

        <div class="card">

            <h3>
                User choice
            </h3>

            <p>
                The model selector allows users to choose
                the available model that best fits their
                current task.
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

text = text[:models_start] + models_section + text[models_end:]


# ============================================================
# CURRENT CAPABILITIES SECTION
# ============================================================

if "Current QntaAI capabilities" not in text:

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
            modes, conversation history, and a web-based
            interface.
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
                The QntaAI interface supports attaching
                files to conversations where supported
                by the application.
            </p>

        </div>

        <div class="card">

            <h3>
                Responsive interface
            </h3>

            <p>
                The web interface is designed to work
                across desktop and mobile screen sizes.
            </p>

        </div>

        <div class="card">

            <h3>
                Web deployment
            </h3>

            <p>
                QntaAI can be deployed as a web application
                with its frontend and backend operating
                together.
            </p>

        </div>

    </div>

</section>


'''

    # Insert before the Architecture section by heading,
    # not by a fragile CSS comment marker.
    architecture_match = re.search(
        r'<section\b[^>]*>[\s\S]*?<h2>\s*How QntaAI works\s*</h2>',
        text,
        flags=re.IGNORECASE
    )

    if architecture_match:
        architecture_section_start = architecture_match.start()
        text = (
            text[:architecture_section_start]
            + capabilities
            + text[architecture_section_start:]
        )
    else:
        # Fallback: insert before Project Structure.
        project_match = re.search(
            r'<section\b[^>]*>[\s\S]*?<h2>\s*Project structure\s*</h2>',
            text,
            flags=re.IGNORECASE
        )

        if project_match:
            project_start = project_match.start()
            text = (
                text[:project_start]
                + capabilities
                + text[project_start:]
            )
        else:
            raise SystemExit(
                "ERROR: Could not find a safe location for "
                "Capabilities section."
            )


# ============================================================
# UPDATE PROJECT STRUCTURE
# ============================================================

old_structure_pattern = re.compile(
    r'<pre>\s*'
    r'QntaAI[\s\S]*?'
    r'QntaAI Official Documentation'
    r'\s*</pre>',
    flags=re.IGNORECASE
)

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

if old_structure_pattern.search(text):
    text = old_structure_pattern.sub(
        new_structure,
        text,
        count=1
    )


# ============================================================
# UPDATE FAQ
# ============================================================

text = re.sub(
    r'(<summary>\s*Which AI models are available\?\s*</summary>\s*'
    r'<p>)[\s\S]*?(</p>)',
    r'''\1
            QntaAI provides a multi-model selector with
            multiple supported models available through
            the backend. The available catalog can change
            as model availability changes.
        \2''',
    text,
    count=1,
    flags=re.IGNORECASE
)


# ============================================================
# ADD CODE STYLING
# ============================================================

if "DOCUMENTATION ENHANCEMENTS" not in text:

    css = r'''        /* =========================================
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

    head_style_end = text.find("</style>")

    if head_style_end == -1:
        raise SystemExit("ERROR: </style> not found.")

    text = (
        text[:head_style_end]
        + "\n"
        + css
        + text[head_style_end:]
    )


# ============================================================
# BACK-TO-TOP
# ============================================================

if 'class="back-to-top"' not in text:

    back_to_top = r'''
<a
    class="back-to-top"
    href="#top"
    aria-label="Back to top"
    title="Back to top"
>
    ↑
</a>

'''

    body_end = "</body>"

    if body_end not in text:
        raise SystemExit("ERROR: </body> not found.")

    text = text.replace(
        body_end,
        back_to_top + body_end,
        1
    )


# ============================================================
# TOP ANCHOR
# ============================================================

if '<body id="top">' not in text:

    text = text.replace(
        "<body>",
        '<body id="top">',
        1
    )


# ============================================================
# CLEANUP
# ============================================================

text = re.sub(
    r"\n{4,}",
    "\n\n\n",
    text
)

HTML.write_text(text, encoding="utf-8")


# ============================================================
# VERIFICATION
# ============================================================

print()
print("==========================================")
print(" QntaAI DOCUMENTATION UPGRADE COMPLETE")
print("==========================================")
print()

checks = [
    (
        "Models section",
        'id="models"' in text
    ),
    (
        "Correct surname",
        "Suryansh Singh Bhadouriya" in text
    ),
    (
        "Capabilities section",
        "Current QntaAI capabilities" in text
    ),
    (
        "Back-to-top",
        'class="back-to-top"' in text
    ),
    (
        "Model selector wording",
        "model selector" in text.lower()
    ),
    (
        "Nemotron 3 Super",
        "nvidia/nemotron-3-super-120b-a12b:free" in text
    ),
    (
        "No emoji characters",
        not emoji_pattern.search(text)
    ),
]

for name, ok in checks:
    print(
        f"  [{'OK' if ok else 'FAIL'}] {name}"
    )

print()
print("Backup:")
print(" ", BACKUP.name)
print()
