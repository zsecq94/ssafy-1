import "./header.scss";
import {Link} from "react-router-dom";

const Header = () => {
  return (
    <div className="header-wrapper">
      <div className="header-title">
        <Link to="/">
          <span>I GoAT</span>
        </Link>
      </div>
      <div className="header-menu">
        <Link to="board-list">Community</Link>
        <Link to="create-board">Writing</Link>
        <Link to="/login">Log In</Link>
        <Link to="/register">Sign Up</Link>
      </div>
    </div>
  );
};

export default Header;