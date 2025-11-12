"use client"

import { motion } from "framer-motion"
import ParticlesBackground from "./ParticlesBackground"
import { Brain, Cloud, Rocket, Shield, Settings, Zap } from "lucide-react"

const FeatureCard = ({ icon: Icon, title, description, index }) => {
  const cardVariants = {
    initial: { opacity: 0, y: 50 },
    animate: {
      opacity: 1,
      y: 0,
      transition: {
        delay: index * 0.1,
        type: "spring",
        stiffness: 100,
        damping: 15,
      },
    },
    hover: {
      scale: 1.02,
      transition: { duration: 0.3 },
    },
  }

  return (
    <motion.div
      className="glow-border bg-[#1a1a2e] rounded-2xl p-8 text-center relative overflow-hidden group"
      variants={cardVariants}
      initial="initial"
      whileInView="animate"
      whileHover="hover"
      viewport={{ once: true, amount: 0.3 }}
    >
      <div className="relative z-10">
        <Icon className="w-16 h-16 text-purple-400 mx-auto mb-4 stroke-[1.5]" />
        <h3 className="text-2xl font-space-grotesk text-white font-bold mb-3">{title}</h3>
        <p className="text-gray-400 font-inter leading-relaxed">{description}</p>
      </div>

      {/* Dot indicators at bottom */}
      <div className="flex justify-center gap-2 mt-6">
        {[...Array(6)].map((_, i) => (
          <div key={i} className={`w-2 h-2 rounded-full ${i === index % 6 ? "bg-purple-500" : "bg-gray-600"}`} />
        ))}
      </div>
    </motion.div>
  )
}

export default function FeatureCardsSection() {
  const features = [
    {
      icon: Brain,
      title: "Intuitive AI Design",
      description: "Leverage powerful AI to generate stunning UI/UX designs instantly, tailored to your needs.",
    },
    {
      icon: Cloud,
      title: "Seamless Cloud Integration",
      description: "Deploy your AI-powered applications effortlessly to your cloud with pop up built in to your needs.",
    },
    {
      icon: Rocket,
      title: "Rapid Prototyping",
      description: "Accelerate your development workflow with quick prototypes and iterative design cycles.",
    },
    {
      icon: Shield,
      title: "Secure & Scalable",
      description: "Build with confidence on a robust infrastructure designed for security and scalability.",
    },
    {
      icon: Settings,
      title: "Customizable Components",
      description: "Tailor every aspect of your generated layouts with flexible and reusable components.",
    },
    {
      icon: Zap,
      title: "Performance Optimized",
      description: "Ensure your applications run at peak performance with automatically optimized code.",
    },
  ]

  return (
    <section id="features" className="relative py-20 overflow-hidden">
      <ParticlesBackground />

      <div className="relative z-10 container mx-auto px-6">
        <motion.h2
          className="text-5xl md:text-6xl font-bold font-space-grotesk text-center mb-16 text-white"
          initial={{ opacity: 0, y: -30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
        >
          Key Features
        </motion.h2>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <FeatureCard
              key={feature.title}
              icon={feature.icon}
              title={feature.title}
              description={feature.description}
              index={index}
            />
          ))}
        </div>
      </div>
    </section>
  )
}
