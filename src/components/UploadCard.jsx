function UploadCard() {
  return (
    <div className="bg-slate-900 rounded-2xl p-8 shadow-2xl border border-slate-700">

      <h2 className="text-3xl font-bold text-white mb-2">
        Upload Your Project
      </h2>

      <p className="text-gray-400 mb-8">
        Upload ZIP files for quantum security analysis
      </p>

      <div className="border-2 border-dashed border-blue-500 rounded-xl p-12 text-center hover:border-purple-500 transition">

        <div className="text-6xl mb-4">
            ☁️
        </div>

        <p className="text-white text-lg">
          Drag & Drop ZIP here
        </p>

        <p className="text-gray-400 my-4">
          or
        </p>

        <button
          className="bg-gradient-to-r from-purple-600 to-blue-600 px-8 py-3 rounded-xl text-white font-semibold hover:scale-105 transition"
        >
          Browse Files
        </button>

      </div>

    </div>
  )
}

export default UploadCard;