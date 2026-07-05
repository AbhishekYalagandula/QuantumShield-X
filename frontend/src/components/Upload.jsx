import "./Upload.css";
import { useRef, useState } from "react";

function Upload() {
  const fileInputRef = useRef();

  const [selectedFile, setSelectedFile] = useState(null);

  const handleBrowse = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];

    if (file) {
      setSelectedFile(file);
    }
  };

  return (
    <div className="upload-page">

      <div className="upload-card">

        <h1>Upload Your Project</h1>

        <p>Upload your ZIP project for Quantum Security Analysis</p>

        <div className="drop-area">

          <div className="cloud">☁️</div>

          <h3>Drag & Drop ZIP File Here</h3>

          <p>or</p>

          <button
            className="browse-btn"
            onClick={handleBrowse}
          >
            Browse Files
          </button>

          <input
            type="file"
            accept=".zip"
            ref={fileInputRef}
            onChange={handleFileChange}
            style={{ display: "none" }}
          />

        </div>

        {selectedFile && (

          <div className="file-card">

            <h3>📦 {selectedFile.name}</h3>

            <p>
{
selectedFile.size > 1024*1024
?

`${(selectedFile.size/(1024*1024)).toFixed(2)} MB`

:

`${(selectedFile.size/1024).toFixed(2)} KB`

}
</p>

            <button className="scan-btn">
              Upload & Scan
            </button>

          </div>

        )}

      </div>

    </div>
  );
}

export default Upload;