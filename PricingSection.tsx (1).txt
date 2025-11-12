"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import ParticlesBackground from "./ParticlesBackground"

const IconCheck = () => (
  <svg className="w-5 h-5 text-green-400 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7"></path>
  </svg>
)

interface Plan {
  name: string
  description: string
  priceUSD: number
  priceBDT: number
  features: string[]
  isPopular?: boolean
}

interface PricingCardProps {
  plan: Plan
  currency: string
  isPopular?: boolean
  index: number
}

function PricingCard({ plan, currency, isPopular, index }: PricingCardProps) {
  const isUSD = currency === "USD"
  const price = isUSD ? plan.priceUSD : plan.priceBDT
  const currencySymbol = isUSD ? "$" : "৳"

  const cardVariants = {
    initial: { opacity: 0, y: 50 },
    animate: {
      opacity: 1,
      y: 0,
      transition: {
        delay: index * 0.15,
        type: "spring",
        stiffness: 100,
        damping: 15,
      },
    },
    hover: {
      scale: 1.05,
      boxShadow: "0 0 35px rgba(147, 51, 234, 0.8)",
      transition: { duration: 0.3 },
    },
  }

  const buttonHoverVariants = {
    hover: {
      scale: 1.03,
      boxShadow: "0 0 15px rgba(147, 51, 234, 0.6)",
      transition: { duration: 0.3 },
    },
  }

  return (
    <motion.div
      className={`bg-[#1F2937] border-2 rounded-xl p-8 flex flex-col items-center text-center relative overflow-hidden shadow-2xl ${
        isPopular ? "border-purple-600" : "border-[#374151]"
      }`}
      variants={cardVariants}
      initial="initial"
      whileInView="animate"
      whileHover="hover"
      viewport={{ once: true, amount: 0.3 }}
    >
      {isPopular && (
        <span className="absolute top-0 right-0 bg-purple-600 text-white text-xs font-bold px-3 py-1 rounded-bl-lg">
          Popular
        </span>
      )}
      <h3 className="text-3xl font-space-grotesk text-white mb-4">{plan.name}</h3>
      <p className="text-gray-400 font-inter mb-6">{plan.description}</p>
      <div className="flex items-baseline mb-8">
        <span className="text-5xl font-extrabold font-space-grotesk text-purple-500">
          {currencySymbol}
          {price}
        </span>
        <span className="text-lg text-gray-500 ml-2">/ month</span>
      </div>
      <ul className="text-gray-300 font-inter text-left space-y-3 mb-10 w-full">
        {plan.features.map((feature, i) => (
          <li key={i} className="flex items-start">
            <IconCheck />
            <span>{feature}</span>
          </li>
        ))}
      </ul>
      <motion.button
        className={`mt-auto w-full py-3 rounded-lg text-lg font-bold transition-all duration-300 relative group overflow-hidden ${
          isPopular ? "bg-purple-600 text-white hover:bg-purple-700" : "bg-gray-700 text-gray-200 hover:bg-gray-600"
        }`}
        variants={buttonHoverVariants}
        whileHover="hover"
      >
        Choose {plan.name}
        <span className="absolute inset-0 bg-gradient-to-br from-purple-400 via-purple-600 to-purple-800 opacity-0 group-hover:opacity-20 transition-opacity duration-500"></span>
      </motion.button>
    </motion.div>
  )
}

export default function PricingSection() {
  const [currency, setCurrency] = useState("USD")

  const pricingPlans = [
    {
      name: "Starter",
      description: "Perfect for small projects",
      priceUSD: 29,
      priceBDT: 2999,
      features: ["5 AI Generations/month", "Basic UI Components", "Email Support", "Email Support", "1 User Account"],
    },
    {
      name: "Pro",
      description: "Great for medium-sized businesses",
      priceUSD: 79,
      priceBDT: 7999,
      isPopular: true,
      features: [
        "Unlimited AI Generations",
        "Advanced UI Components",
        "Priority Chat Support",
        "5 User Accounts",
        "Custom Themes",
      ],
    },
    {
      name: "Enterprise",
      description: "Best for large organizations",
      priceUSD: 199,
      priceBDT: 19999,
      features: [
        "All Pro Features",
        "Dedicated Account Manager",
        "On-demand Training",
        "Unlimited Users",
        "SLA & Uptime Guarantee",
      ],
    },
  ]

  return (
    <section id="pricing" className="relative py-20 overflow-hidden">
      <ParticlesBackground />

      <div className="relative z-10 container mx-auto px-6">
        <motion.h2
          className="text-5xl md:text-6xl font-bold font-space-grotesk text-center mb-4 text-white"
          initial={{ opacity: 0, y: -30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
        >
          Flexible Pricing
        </motion.h2>
        <motion.p
          className="text-xl text-gray-400 text-center mb-12 font-inter"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
        >
          Choose a plan that fits your needs. Scale up as your AI projects grow.
        </motion.p>

        {/* Currency Toggle */}
        <motion.div
          className="flex justify-center mb-12"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
        >
          <div className="inline-flex bg-[#2d2d44] rounded-full p-1">
            <button
              className={`px-8 py-3 rounded-full font-bold transition-all ${
                currency === "USD" ? "bg-purple-600 text-white" : "text-gray-400"
              }`}
              onClick={() => setCurrency("USD")}
            >
              USD ($)
            </button>
            <button
              className={`px-8 py-3 rounded-full font-bold transition-all ${
                currency === "BDT" ? "bg-purple-600 text-white" : "text-gray-400"
              }`}
              onClick={() => setCurrency("BDT")}
            >
              BDT (৳)
            </button>
          </div>
        </motion.div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {pricingPlans.map((plan, index) => (
            <PricingCard key={plan.name} plan={plan} currency={currency} isPopular={plan.isPopular} index={index} />
          ))}
        </div>
      </div>
    </section>
  )
}
