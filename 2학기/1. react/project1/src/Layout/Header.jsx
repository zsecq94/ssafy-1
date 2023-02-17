import * as React from 'react';
import { Link } from 'react-router-dom';

// MUI
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';


const Header = () => {

    return (
        <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
            <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                Logo
            </Typography>
            <Button color="inherit" variant="h6" ><Link to='/' style={{ textDecoration: "none", color: 'white' }}>Vote</Link></Button>
            <Button color="inherit" variant="h6" ><Link to='/myvote' style={{ textDecoration: "none", color: 'white' }}>My Vote</Link></Button>
            <Button color="inherit" variant="h6" ><Link to='/createvote' style={{ textDecoration: "none", color: 'white'  }}>Create a Vote</Link></Button>
            </Toolbar>
        </AppBar>
        </Box>
    );
}

export default Header;