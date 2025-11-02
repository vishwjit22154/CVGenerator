import { useState } from 'react';
import { Toaster } from 'react-hot-toast';
import Header from './components/Header';
import CoverLetterForm from './components/CoverLetterForm';
import CoverLetterPreview from './components/CoverLetterPreview';

function App() {
  const [generatedLetter, setGeneratedLetter] = useState(null);
  const [formData, setFormData] = useState(null);

  return (
    <div className="min-h-screen">
      <Toaster position="top-right" />
      
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-7xl">
        {!generatedLetter ? (
          <div className="space-y-8">
            <div className="text-center max-w-2xl mx-auto mb-8">
              <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-3">
                Generate Professional Cover Letters
              </h2>
              <p className="text-lg text-gray-600">
                Paste your resume and job posting. AI handles the rest.
              </p>
            </div>
            
            <CoverLetterForm 
              onGenerate={(letter, data) => {
                setGeneratedLetter(letter);
                setFormData(data);
              }} 
            />
          </div>
        ) : (
          <CoverLetterPreview 
            letter={generatedLetter}
            formData={formData}
            onReset={() => {
              setGeneratedLetter(null);
              setFormData(null);
            }}
          />
        )}
      </main>
      
      <footer className="bg-white border-t border-gray-200 mt-16">
        <div className="container mx-auto px-4 py-6 text-center text-gray-500 text-sm">
          <p>© 2025 AI Cover Letter Generator</p>
          <p className="mt-1">Built by Hvishwajit</p>
        </div>
      </footer>
    </div>
  );
}

export default App;

