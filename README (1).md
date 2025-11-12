# eT's AI Builder

Build your AI future, effortlessly. A modern AI-powered UI builder with multi-model support using Puter API.

## Features

- **Multi-Model AI Support**: Choose from Claude, Gemini, Mistral, and Perplexity models
- **Real-time Preview**: See your generated UI instantly
- **Puter Cloud Deploy**: One-click deployment to free cloud hosting
- **Beautiful Dark UI**: Stunning purple-themed interface with particle effects
- **v0.dev-style Workflow**: Text prompt → AI generation → Live preview → Deploy

## Tech Stack

- **Framework**: Next.js 16 with React 19
- **Styling**: Tailwind CSS v4
- **Animations**: Framer Motion & tsParticles
- **AI**: Puter API (Claude, Gemini, Mistral, Perplexity)
- **Deployment**: Vercel + Puter Cloud

## Getting Started

### Prerequisites

- Node.js 18+ installed
- No API keys required! Puter uses the "User-Pays" model

### Installation

1. Clone the repository:
\`\`\`bash
git clone https://github.com/awesometjms-tech/etai-builder.git
cd etai-builder
\`\`\`

2. Install dependencies:
\`\`\`bash
npm install
\`\`\`

3. Run the development server:
\`\`\`bash
npm run dev
\`\`\`

4. Open [http://localhost:3000](http://localhost:3000)

## AI Models Available

### Claude (Anthropic)
- Claude Sonnet 4.5 - Balanced performance and speed
- Claude Opus 4.1 - Most capable model
- Claude Haiku 4.5 - Fastest responses

### Gemini (Google)
- Gemini 2.5 Flash - Fast and efficient
- Gemini 2.5 Pro - Advanced reasoning
- Gemini 2.0 Flash - Latest generation

### Mistral
- Mistral Large - Complex tasks
- Mistral Medium - Balanced performance
- Codestral - Specialized for code

### Perplexity
- Sonar - Research capabilities
- Sonar Pro - Professional research

## Project Structure

\`\`\`
ets-ai-builder/
├── app/
│   ├── layout.tsx              # Root layout with Puter SDK
│   ├── page.tsx                # Home page
│   └── globals.css             # Dark purple theme
├── components/
│   ├── Header.tsx              # Navigation with logo
│   ├── HeroSection.tsx         # Hero with AI shield
│   ├── FeatureCardsSection.tsx # Glowing feature cards
│   ├── AIBuilderPage.tsx       # Main AI builder interface
│   ├── LivePreviewPane.tsx     # Live preview iframe
│   ├── PuterCloudDeploy.tsx    # One-click deployment
│   ├── PricingSection.tsx      # Pricing with currency toggle
│   ├── TestimonialsSection.tsx # User testimonials
│   ├── Footer.tsx              # Footer with links
│   └── ParticlesBackground.tsx # Animated particles
├── lib/
│   ├── puterAI.ts              # Multi-model AI integration
│   └── types.ts                # TypeScript definitions
└── README.md
\`\`\`

## Usage

1. **Select an AI model** from the dropdown (Claude, Gemini, Mistral, or Perplexity)
2. **Describe your UI** in the text area (e.g., "Create a modern pricing section")
3. **Click "Generate UI"** to create your interface
4. **View the live preview** and generated code side-by-side
5. **Deploy to Puter Cloud** with one click for free hosting

## Puter Integration

This project uses [Puter.js](https://docs.puter.com) for **keyless AI access**:

### 🔑 Keyless API Mode - No API Keys Required!

When running on Puter or with the Puter SDK loaded:

1. **Free, Unlimited AI Access** - Claude, Gemini, Mistral, and Perplexity
2. **Zero Configuration** - No API keys, no environment variables
3. **Automatic Detection** - App detects Puter environment and enables keyless mode
4. **One-Click Deploy** - Deploy generated UIs instantly to Puter hosting

The Puter SDK is loaded in `app/layout.tsx`:

\`\`\`tsx
<Script src="https://js.puter.com/v2/" strategy="afterInteractive" />
\`\`\`

### How It Works

- **On Puter**: Automatically uses keyless APIs via `puter.ai.chat()`
- **Local Dev**: Shows fallback UI until Puter SDK loads
- **Status Indicator**: Green badge shows "Keyless API Active" when ready

### Supported Models

All models are accessed **without API keys** through Puter:

- **Claude**: `claude-sonnet-4-5`, `claude-opus-4-1`, `claude-3-7-sonnet`
- **Gemini**: `gemini-2.5-flash`, `gemini-2.5-pro`, `gemini-2.0-flash`
- **Mistral**: `mistral-large`, `mistral-medium`, `codestral`
- **Perplexity**: `sonar`, `sonar-pro`

## Environment Variables

**None required!** Puter handles everything through the SDK.

## Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/awesometjms-tech/etai-builder)

## License

MIT License - feel free to use this project for your own applications!

## Credits

Built with ❤️ using v0.dev, Next.js, and Puter API

## Learn More

- [Free Claude API Tutorial](https://developer.puter.com/tutorials/free-unlimited-claude-35-sonnet-api/)
- [Free Gemini API Tutorial](https://developer.puter.com/tutorials/free-gemini-api/)
- [Free Mistral API Tutorial](https://developer.puter.com/tutorials/free-unlimited-mistral-api/)
- [Free Perplexity API Tutorial](https://developer.puter.com/tutorials/free-unlimited-perplexity-ai-api/)
- [Puter Documentation](https://docs.puter.com)
- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS](https://tailwindcss.com)
- [Framer Motion](https://www.framer.com/motion)
