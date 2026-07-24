import "./Upload.css";

import { useState } from "react";
import Navbar from "../components/Navbar/Navbar";

import {
    MdCloudUpload,
    MdInsertDriveFile,
    MdClose,
    MdInfo,
    MdArrowForward
} from "react-icons/md";

import axios from "axios";

function Upload() {

    const [selectedFile, setSelectedFile] = useState(null);

    const [loading, setLoading] = useState(false);

const [result, setResult] = useState(null);

    const [dragActive, setDragActive] = useState(false);

    const handleFileSelect = (event) => {

        const file = event.target.files[0];

        if (file) {

            setSelectedFile(file);

        }

    };

    const handleDrop = (event) => {

        event.preventDefault();

        setDragActive(false);

        const file = event.dataTransfer.files[0];

        if (file) {

            setSelectedFile(file);

        }

    };

    const handleDragOver = (event) => {

        event.preventDefault();

        setDragActive(true);

    };

    const handleDragLeave = () => {

        setDragActive(false);

    };

    const removeFile = () => {

        setSelectedFile(null);

    };
    const uploadProject = async () => {

    if (!selectedFile) return;

    const formData = new FormData();

    formData.append("file", selectedFile);

    try {

        setLoading(true);

        const response = await axios.post(

            "http://127.0.0.1:8000/upload",

            formData,

            {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            }

        );

        setResult(response.data);

        alert("Project uploaded successfully!");

    }

    catch (err) {

        console.log(err);

        alert("Upload Failed");

    }

    finally {

        setLoading(false);

    }

};

    return (

        <>

            <Navbar />

            <main className="upload-page">

                <section className="upload-header">

                    <h1>

                        Upload Your Project

                    </h1>

                    <p>

                        Upload your ZIP project for QuantumShield-X Analysis

                    </p>

                </section>

                <section className="upload-card">

                    <div

                        className={`upload-area ${dragActive ? "active" : ""}`}

                        onDrop={handleDrop}

                        onDragOver={handleDragOver}

                        onDragLeave={handleDragLeave}

                    >

                        <MdCloudUpload className="upload-icon" />

                        <h2>

                            Drag & Drop ZIP File

                        </h2>

                        <p>

                            or

                        </p>

                        <label

                            htmlFor="fileUpload"

                            className="browse-btn"

                        >

                            Browse Files

                        </label>

                        <input

                            id="fileUpload"

                            type="file"

                            accept=".zip"

                            hidden

                            onChange={handleFileSelect}

                        />

                    </div>

                    {

                        selectedFile && (

                            <div className="selected-file">

                                <div className="file-left">

                                    <MdInsertDriveFile className="file-icon" />

                                    <div>

                                        <h3>

                                            {selectedFile.name}

                                        </h3>

                                        <span>

                                            {(selectedFile.size / 1024 / 1024).toFixed(2)} MB

                                        </span>

                                    </div>

                                </div>

                                <button

                                    className="remove-btn"

                                    onClick={removeFile}

                                >

                                    <MdClose />

                                </button>

                            </div>

                        )

                    }
                                        <div className="upload-info">

                        <div className="info-card">

                            <MdInfo className="info-icon"/>

                            <div>

                                <h3>

                                    Supported Files

                                </h3>

                                <p>

                                    ZIP files up to 500MB

                                </p>

                                <span>

                                    Supports Python, Java, C++, JavaScript, React, Node.js and more.

                                </span>

                            </div>

                        </div>

                    </div>

                    <button
className="upload-scan-btn"
disabled={!selectedFile || loading}
onClick={uploadProject}
>

                       {loading ? "Scanning..." : "Upload & Scan"}

                        <MdArrowForward/>

                    </button>

                </section>

            </main>

        </>

    );

}

export default Upload;