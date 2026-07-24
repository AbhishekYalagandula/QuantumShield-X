import { useEffect, useState } from "react";
import axios from "axios";

const [projects, setProjects] = useState([]);

useEffect(() => {

    axios
        .get("http://127.0.0.1:8000/risk/")
        .then((res) => {
            setProjects(res.data);
        })
        .catch((err) => console.log(err));

}, []);