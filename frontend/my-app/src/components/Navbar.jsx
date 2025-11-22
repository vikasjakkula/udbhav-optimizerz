import { NavLink } from 'react-router-dom'

const navItems = [
  { label: 'Home', to: '/home' },
  { label: 'Dashboard', to: '/dashboard' },
  { label: 'Predict', to: '/predict' },
  { label: 'About', to: '/about' },
  { label: 'Feedback', to: '/feedback' }
]

function Navbar() {
  return (
    <nav className="global-navbar">
      <div
        className="brand"
        style={{
          fontWeight: '700',
        }}
      >
        Cardio360
      </div>
      <div className="nav-links">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) =>
              `nav-link ${isActive ? 'nav-link--active' : ''}`
            }
          >
            {item.label}
          </NavLink>
        ))}
      </div>
      <div className="nav-end">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="40"
          height="40"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className="lucide-heart-pulse lucide-heart-pulse-icon"
        >
          <path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>
          <path d="M3.22 13H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/>
        </svg>
      </div>
    </nav>
  )
}

export default Navbar

