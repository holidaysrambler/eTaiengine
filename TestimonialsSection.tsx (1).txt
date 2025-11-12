"use client"

import { motion } from "framer-motion"
import ParticlesBackground from "./ParticlesBackground"

const StarIcon = ({ filled }: { filled: boolean }) => (
  <svg className={`w-5 h-5 ${filled ? "text-yellow-400" : "text-gray-600"}`} fill="currentColor" viewBox="0 0 20 20">
    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
  </svg>
)

interface Testimonial {
  id: number
  quote: string
  name: string
  title: string
  rating: number
  avatar: string
}

interface TestimonialCardProps {
  testimonial: Testimonial
  index: number
}

function TestimonialCard({ testimonial, index }: TestimonialCardProps) {
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
      scale: 1.03,
      boxShadow: "0 0 25px rgba(147, 51, 234, 0.7)",
      transition: { duration: 0.3 },
    },
  }

  return (
    <motion.div
      className="bg-[#1F2937] border border-[#374151] rounded-xl p-8 shadow-xl flex flex-col justify-between relative overflow-hidden group"
      variants={cardVariants}
      initial="initial"
      whileInView="animate"
      whileHover="hover"
      viewport={{ once: true, amount: 0.3 }}
    >
      <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-purple-800/10 to-transparent pointer-events-none opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>

      <div className="flex mb-4 justify-center sm:justify-start">
        {[...Array(5)].map((_, i) => (
          <StarIcon key={i} filled={i < testimonial.rating} />
        ))}
      </div>

      <p className="text-gray-300 font-inter text-lg leading-relaxed mb-6 italic">&ldquo;{testimonial.quote}&rdquo;</p>

      <div className="flex items-center mt-auto">
        <img
          src={testimonial.avatar || "/placeholder.svg"}
          alt={testimonial.name}
          className="w-12 h-12 rounded-full object-cover mr-4 border-2 border-purple-500"
        />
        <div>
          <p className="font-space-grotesk text-white font-semibold text-lg">{testimonial.name}</p>
          <p className="font-inter text-gray-400 text-sm">{testimonial.title}</p>
        </div>
      </div>
    </motion.div>
  )
}

export default function TestimonialsSection() {
  const testimonials: Testimonial[] = [
    {
      id: 1,
      quote:
        "eT's AI Builder has revolutionized our design process. The speed and quality of generated layouts are simply astonishing. It's an indispensable tool!",
      name: "Sarah Chen",
      title: "Lead Product Designer @ InnovateTech",
      rating: 5,
      avatar: "https://randomuser.me/api/portraits/women/32.jpg",
    },
    {
      id: 2,
      quote:
        "We've cut down our prototyping time by 50% since using eT's AI. The intelligent suggestions and customizable components are a game-changer.",
      name: "Michael Wong",
      title: "CTO @ NextGen Solutions",
      rating: 4,
      avatar: "https://randomuser.me/api/portraits/men/44.jpg",
    },
    {
      id: 3,
      quote:
        "The interface is intuitive, and the results are consistently impressive. Our clients are always amazed by how quickly we can bring their visions to life.",
      name: "Jessica Lee",
      title: "Creative Director @ Visionary Studios",
      rating: 5,
      avatar: "https://randomuser.me/api/portraits/women/68.jpg",
    },
    {
      id: 4,
      quote:
        "As a freelancer, this tool helps me deliver high-quality designs faster, allowing me to take on more projects and satisfy more clients.",
      name: "David Kim",
      title: "Freelance UI/UX Designer",
      rating: 4,
      avatar: "https://randomuser.me/api/portraits/men/70.jpg",
    },
    {
      id: 5,
      quote:
        "The scalability and integration options are top-notch. It fits perfectly into our existing workflow and significantly boosts our team's productivity.",
      name: "Emily Johnson",
      title: "VP Engineering @ Global Innovations",
      rating: 5,
      avatar: "https://randomuser.me/api/portraits/women/80.jpg",
    },
    {
      id: 6,
      quote:
        "Initially skeptical, but eT's AI Builder exceeded all expectations. It truly understands design principles and applies them intelligently.",
      name: "Chris Green",
      title: "Senior Developer @ TechCore",
      rating: 4,
      avatar: "https://randomuser.me/api/portraits/men/82.jpg",
    },
  ]

  return (
    <section id="testimonials" className="relative w-full py-20 bg-[#0F172A] text-white overflow-hidden">
      <ParticlesBackground />

      <div className="container mx-auto px-6 relative z-10">
        <motion.h2
          className="text-4xl md:text-5xl font-extrabold font-space-grotesk text-center mb-6 text-purple-400"
          initial={{ opacity: 0, y: -50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.5 }}
        >
          What Our Users Say
        </motion.h2>
        <motion.p
          className="text-xl text-gray-400 text-center mb-16 font-inter max-w-2xl mx-auto"
          initial={{ opacity: 0, y: -30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          Hear directly from professionals who are transforming their design and development with our AI.
        </motion.p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {testimonials.map((testimonial, index) => (
            <TestimonialCard key={testimonial.id} testimonial={testimonial} index={index} />
          ))}
        </div>
      </div>
    </section>
  )
}
