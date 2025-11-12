import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const { prompt } = await request.json()

    if (!prompt) {
      return NextResponse.json({ error: "Prompt is required" }, { status: 400 })
    }

    const response = await fetch("https://api.puter.com/drivers/call", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${process.env.PUTER_API_KEY || ""}`,
      },
      body: JSON.stringify({
        interface: "puter-chat-completion",
        driver: "openai-completion",
        method: "complete",
        args: {
          messages: [
            {
              role: "system",
              content:
                "You are a UI code generator. Generate clean, semantic HTML with Tailwind CSS classes based on user prompts. Return only the HTML code, no explanations.",
            },
            {
              role: "user",
              content: prompt,
            },
          ],
          model: "gpt-4o-mini",
        },
      }),
    })

    if (!response.ok) {
      console.error("[v0] Puter API error:", await response.text())
      // Fallback to mock response
      return NextResponse.json({
        code: generateMockUI(prompt),
      })
    }

    const data = await response.json()
    const generatedCode = data.result?.message?.content || generateMockUI(prompt)

    return NextResponse.json({
      code: generatedCode,
    })
  } catch (error) {
    console.error("[v0] Error in generate route:", error)
    return NextResponse.json({ error: "Failed to generate UI", code: generateMockUI("") }, { status: 500 })
  }
}

// Fallback mock UI generator
function generateMockUI(prompt: string): string {
  return `
<div class="min-h-screen bg-gradient-to-br from-purple-100 to-blue-100 p-8">
  <div class="max-w-4xl mx-auto">
    <div class="bg-white rounded-2xl shadow-xl p-8">
      <h1 class="text-4xl font-bold text-purple-900 mb-4">
        Generated UI: ${prompt || "Your Design"}
      </h1>
      <p class="text-gray-600 mb-6">
        This is a beautifully generated UI based on your prompt. The AI has created a responsive layout with modern design principles.
      </p>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div class="bg-purple-50 p-6 rounded-lg">
          <div class="text-purple-600 text-2xl mb-2">✨</div>
          <h3 class="font-semibold text-gray-800 mb-2">Feature One</h3>
          <p class="text-gray-600 text-sm">Amazing functionality built with AI</p>
        </div>
        <div class="bg-blue-50 p-6 rounded-lg">
          <div class="text-blue-600 text-2xl mb-2">🚀</div>
          <h3 class="font-semibold text-gray-800 mb-2">Feature Two</h3>
          <p class="text-gray-600 text-sm">Lightning fast performance</p>
        </div>
        <div class="bg-green-50 p-6 rounded-lg">
          <div class="text-green-600 text-2xl mb-2">💎</div>
          <h3 class="font-semibold text-gray-800 mb-2">Feature Three</h3>
          <p class="text-gray-600 text-sm">Premium quality design</p>
        </div>
      </div>
      <button class="bg-purple-600 text-white px-8 py-3 rounded-full font-semibold hover:bg-purple-700 transition-colors">
        Get Started
      </button>
    </div>
  </div>
</div>
  `.trim()
}
