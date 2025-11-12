"use client"

import { motion } from "framer-motion"
import ParticlesBackground from "./ParticlesBackground"
import Link from "next/link"
import Image from "next/image"

export default function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center justify-center text-white overflow-hidden pt-20">
      <ParticlesBackground />

      <div className="relative z-10 container mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center">
        {/* Left Content */}
        <motion.div initial={{ opacity: 0, x: -50 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.7 }}>
          <h1 className="text-5xl md:text-7xl font-bold font-space-grotesk mb-6 leading-tight">
            Build Your AI Future, Effortlessly
            <span className="text-purple-400">lessly</span>
          </h1>
          <p className="text-xl text-gray-300 font-inter mb-8 leading-relaxed">
            eT's AI Builder empowers you to design, deploy, and scale intelligent solutions with intuitive tools and
            cutting-edge technology.
          </p>
          <div className="flex flex-col sm:flex-row gap-4">
            <Link href="/builder">
              <motion.button
                className="bg-purple-600 text-white px-8 py-4 rounded-xl text-lg font-bold button-glow"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Start Building Now
              </motion.button>
            </Link>
            <Link href="/features">
              <motion.button
                className="bg-gray-800 text-white px-8 py-4 rounded-xl text-lg font-bold border border-gray-700 hover:border-purple-500 transition-colors"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Learn More
              </motion.button>
            </Link>
          </div>
        </motion.div>

        {/* Right Content - Shield with Network */}
        <motion.div
          className="relative flex items-center justify-center"
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.7, delay: 0.2 }}
        >
          <div className="relative w-full max-w-lg aspect-square">
            {/* Shield with glow effect */}
            <div className="absolute inset-0 bg-gradient-to-br from-purple-600/20 to-transparent rounded-full blur-3xl"></div>
            <Image
              src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/unnamed%20%282%29-LRsFW55ldayna66OmYwUHm0csOqmaO.jpg"
              alt="AI Network Shield"
              width={600}
              height={600}
              className="relative z-10 drop-shadow-2xl"
            />
          </div>
        </motion.div>
      </div>
    </section>
  )
}
