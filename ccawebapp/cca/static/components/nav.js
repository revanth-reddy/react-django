import React from 'react';

class Nav extends React.Component {
  render() {
    return (
    	<nav class="navbar navbar-inverse navbar-fixed-top">
		  <div class="container-fluid">
		    <div class="navbar-header">
		      <a class="navbar-brand" href="/">CCA</a>
		      <a class="navbar-brand" href="../wdct">WDCT</a>
		      <a class="navbar-brand" href="../core">CORE</a>
		      <a class="navbar-brand" href="../robo">ROBO</a>
		      <a class="navbar-brand" href="../r&d">R&D</a>
		      <a class="navbar-brand" href="../ecell">ECELL</a>   
		    </div>
		  </div>
		</nav>
    	);
  }
}

export default Nav;