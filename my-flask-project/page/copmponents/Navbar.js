import Link from 'next/link';

const Navbar = ({ isAuthenticated }) => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link className="navbar-brand" href="/">Developer Portfolio</Link>
        <div>
          {isAuthenticated ? (
            <Link href="/logout" className="btn btn-outline-primary">Logout</Link>
          ) : (
            <>
              <Link href="/login" className="btn btn-outline-primary">Login</Link>
              <Link href="/register" className="btn btn-primary ms-2">Register</Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
