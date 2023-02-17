import Header from './Layout/Header';
import Footer from './Layout/Footer';
import Vote from './pages/Vote';
import MyVote from './pages/MyVote';
import CreateVote from './pages/CreateVote';


import { BrowserRouter, Routes, Route } from 'react-router-dom';


const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path='/' element={<Vote />}/>
        <Route path='/myvote' element={<MyVote />}/>
        <Route path='/createvote' element={<CreateVote />}/>
      </Routes>
      
      <Footer />
    </BrowserRouter>
  )
}

export default App;
