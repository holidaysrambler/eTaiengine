"use client"

import { useState } from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import { Menu, X } from "lucide-react"

export default function Header() {
  const [isOpen, setIsOpen] = useState(false)
  const pathname = usePathname()

  const navLinks = [
    { name: "Home", href: "/" },
    { name: "Features", href: "/features" },
    { name: "Pricing", href: "/pricing" },
    { name: "Testimonials", href: "/testimonials" },
  ]

  const isActive = (href: string) => pathname === href

  return (
    <motion.header
      className="fixed w-full top-0 left-0 z-50 bg-[#0a0a0f]/90 backdrop-blur-lg border-b border-purple-500/30"
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <div className="container mx-auto px-6 py-4 flex justify-between items-center">
        {/* Logo with shield icon matching the design */}
        <Link href="/" className="flex items-center gap-3 text-2xl font-bold text-white">
          <motion.div
            className="w-10 h-10 bg-gradient-to-br from-purple-600 to-purple-400 rounded-lg flex items-center justify-center"
            whileHover={{ scale: 1.05 }}
          >
            <span className="text-white font-bold">eT</span>
          </motion.div>
          <span className="font-space-grotesk">eT's AI Builder</span>
        </Link>

        {/* Desktop Nav */}
        <nav className="hidden md:flex items-center gap-8">
          {navLinks.map((link) => (
            <Link
              key={link.name}
              href={link.href}
              className={`font-inter transition-colors ${
                isActive(link.href) ? "text-purple-400 font-semibold" : "text-gray-300 hover:text-purple-400"
              }`}
            >
              {link.name}
            </Link>
          ))}
          <Link href="/builder">
            <motion.button
              className="bg-purple-600 text-white px-6 py-2 rounded-lg font-semibold button-glow"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              Start Building
            </motion.button>
          </Link>
        </nav>

        {/* Mobile Menu Toggle */}
        <button onClick={() => setIsOpen(!isOpen)} className="md:hidden text-white">
          {isOpen ? <X size={28} /> : <Menu size={28} />}
        </button>
      </div>

      {/* Mobile Nav */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            className="md:hidden bg-[#1a1a2e] border-t border-purple-500/30 p-6"
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
          >
            <nav className="flex flex-col gap-4">
              {navLinks.map((link) => (
                <Link
                  key={link.name}
                  href={link.href}
                  className={`py-2 transition-colors ${
                    isActive(link.href) ? "text-purple-400 font-semibold" : "text-gray-300 hover:text-purple-400"
                  }`}
                  onClick={() => setIsOpen(false)}
                >
                  {link.name}
                </Link>
              ))}
              <Link href="/builder" onClick={() => setIsOpen(false)}>
                <button className="w-full bg-purple-600 text-white px-6 py-2 rounded-lg font-semibold mt-4">
                  Start Building
                </button>
              </Link>
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.header>
  )
}
