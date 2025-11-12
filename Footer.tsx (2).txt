"use client"

import { motion } from "framer-motion"
import Link from "next/link"
import { Twitter, Github, Linkedin } from "lucide-react"

export default function Footer() {
  return (
    <motion.footer
      className="relative py-12 overflow-hidden"
      initial={{ opacity: 0 }}
      whileInView={{ opacity: 1 }}
      viewport={{ once: true }}
    >
      <div className="absolute inset-0 border-2 border-purple-500/30 rounded-3xl mx-6 mb-6"></div>

      <div className="relative z-10 container mx-auto px-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Logo and Description */}
          <div className="md:col-span-1">
            <div className="flex items-center gap-2 mb-4">
              <div className="w-10 h-10 bg-gradient-to-br from-purple-600 to-purple-400 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold">eT</span>
              </div>
              <h3 className="text-2xl font-bold font-space-grotesk text-white">eT Builder</h3>
            </div>
            <p className="text-gray-400 font-inter mb-6">
              Revolutionizing design with intelligent AI-powered solutions.
            </p>
            <div className="flex gap-4">
              <a href="#" className="text-purple-400 hover:text-purple-300 transition-colors">
                <Twitter className="w-6 h-6" />
              </a>
              <a href="#" className="text-purple-400 hover:text-purple-300 transition-colors">
                <Github className="w-6 h-6" />
              </a>
              <a href="#" className="text-purple-400 hover:text-purple-300 transition-colors">
                <Linkedin className="w-6 h-6" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-xl font-bold font-space-grotesk text-white mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li>
                <Link href="/features" className="text-gray-400 hover:text-purple-400 transition-colors">
                  Features
                </Link>
              </li>
              <li>
                <Link href="/pricing" className="text-gray-400 hover:text-purple-400 transition-colors">
                  Pricing
                </Link>
              </li>
              <li>
                <Link href="/testimonials" className="text-gray-400 hover:text-purple-400 transition-colors">
                  Testimonials
                </Link>
              </li>
              <li>
                <Link href="/builder" className="text-gray-400 hover:text-purple-400 transition-colors">
                  AI Builder
                </Link>
              </li>
            </ul>
          </div>

          {/* Resources */}
          <div>
            <h4 className="text-xl font-bold font-space-grotesk text-white mb-4">Resources</h4>
            <ul className="space-y-2">
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                  Documentation
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                  Support Center
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                  Integrations
                </a>
              </li>
            </ul>
          </div>

          {/* Documentation */}
          <div>
            <h4 className="text-xl font-bold font-space-grotesk text-white mb-4">Documentation</h4>
            <ul className="space-y-2">
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                  Support Center
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                  API Reference
                </a>
              </li>
              <li>
                <a href="#" className="text-gray-400 hover:text-purple-400 transition-colors">
                  Terms of Service
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-purple-500/30 mt-12 pt-8 text-center">
          <p className="text-gray-500 font-inter">© 2025 eT Builder. All rights reserved.</p>
        </div>
      </div>
    </motion.footer>
  )
}
