import Navbar from '../components/Navbar';

export default function Home() {
  return (
    <div>
      <Navbar isAuthenticated={false} />
      <div className="container mt-4">
        <h1>Welcome to Developer Portfolio</h1>
        <p>Find developers or create your portfolio.</p>
      </div>
    </div>
  );
}
