"use client"

import { useCallback } from "react"
import Particles from "react-tsparticles"
import { loadSlim } from "tsparticles-slim"
import type { Engine } from "tsparticles-engine"

export default function ParticlesBackground() {
  const particlesInit = useCallback(async (engine: Engine) => {
    await loadSlim(engine)
  }, [])

  // <CHANGE> Enhanced particles config with purple nebula effect
  const particlesConfig = {
    background: {
      color: {
        value: "transparent",
      },
    },
    fpsLimit: 120,
    interactivity: {
      events: {
        onClick: {
          enable: false,
        },
        onHover: {
          enable: true,
          mode: "grab",
          parallax: {
            enable: true,
            force: 60,
            smooth: 10,
          },
        },
        resize: true,
      },
      modes: {
        grab: {
          distance: 200,
          links: {
            opacity: 0.3,
            color: "#a855f7",
          },
        },
      },
    },
    particles: {
      color: {
        value: ["#ffffff", "#a855f7", "#9333ea", "#c084fc"],
      },
      links: {
        color: "#a855f7",
        distance: 150,
        enable: true,
        opacity: 0.15,
        width: 1,
      },
      move: {
        direction: "none",
        enable: true,
        outModes: {
          default: "bounce",
        },
        random: true,
        speed: 0.5,
        straight: false,
      },
      number: {
        density: {
          enable: true,
          area: 800,
        },
        value: 120,
      },
      opacity: {
        value: { min: 0.2, max: 0.8 },
        animation: {
          enable: true,
          speed: 1.5,
          sync: false,
          startValue: "random",
          destroy: "none",
        },
      },
      shape: {
        type: ["circle", "triangle"],
      },
      size: {
        value: { min: 1, max: 4 },
        animation: {
          enable: true,
          speed: 3,
          minimumValue: 1,
          sync: false,
          startValue: "random",
          destroy: "none",
        },
      },
    },
    detectRetina: true,
  }

  return (
    <div className="absolute inset-0 w-full h-full pointer-events-none">
      <Particles id="tsparticles" init={particlesInit} options={particlesConfig} />
    </div>
  )
}
