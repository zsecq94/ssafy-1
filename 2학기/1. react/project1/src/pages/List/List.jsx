import React from "react";

// MUI
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';



const List = (props) => {

  const ListItem = props.items

  return (
    ListItem.map((V, index) => (
      <Box key={index} sx={{ padding: '20px', display: 'flex' }}>
        <Card sx={{ maxWidth: 300, maxHeight: 300 }} >
          <CardMedia
            sx={{ height: 150, width: 300 }}
            image={`https://ssafy-viba-s3.s3.ap-northeast-2.amazonaws.com/public/${V.vote_img_url}`}
            title="green iguana"
          />
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
              {V.vote_title}
            </Typography>
            <Typography variant="body2" color="text.secondary">
              {V.vote_desc}
            </Typography>
          </CardContent>
          <CardActions>
            <Button size="small">Choice</Button>
          </CardActions>
        </Card>
      </Box>
    ))
  )
}

export default List;