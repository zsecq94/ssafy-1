import React, { useState, useEffect } from "react";
import ListV from './List/List';

// DATA
import categoryDats from './dump.json'
import ListItem from './List/dump.json'

// MUI
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';

// 카테고리 데이터 받아오기
const useGetCategoryDatas = url => {
    const [data, setData] = useState([]);
  
    const getDatas = async () => {
      
      setData(categoryDats);
    };
  
    useEffect(() => {
      getDatas();
    }, []);
    return data;
};

// MAIN
const Vote = () => {

    const detail = []

    const ShowDetail = (V, V2) => {
        if (V === V2.cat_no) {
            detail.push(V2.cat_title)
            detail.push(V2.cat_desc)
        }
    };

    const categoryDatas = useGetCategoryDatas();

    const [value, setValue] = useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    
    return (
        <Box sx={{ bgcolor: 'background.paper'}}>
            <Tabs
                value={value}
                onChange={handleChange}
                variant="scrollable"
                scrollButtons
                allowScrollButtonsMobile
                aria-label="scrollable force tabs example"
            >
                {categoryDatas.map((categoryDats, index) => (
                    <Tab
                        key={index}
                        sx={{ marginRight: '50px' }}
                        label={categoryDats.cat_title}
                        onClick={ShowDetail(value, categoryDats)}
                    />
                ))}                
            </Tabs>
            <hr />
            <Box sx={{ width: '1000px', height: '200px', padding: '30px'}}>
                <h1>{detail[0]}</h1>
                <h2>{detail[1]}</h2>
            </Box>
            <hr />
            <Tabs
                sx={{ display: 'flex'}}
                variant="scrollable"
                allowScrollButtonsMobile
                aria-label="scrollable force tabs example"
            >
                <ListV {...ListItem} />
            </Tabs>
        </Box>
    )
}

export default Vote;