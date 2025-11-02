import { useState } from 'react';
import { 
  Download, 
  RotateCcw, 
  Copy, 
  Check,
  FileText,
  Tag
} from 'lucide-react';
import toast from 'react-hot-toast';
import { coverLetterAPI } from '../services/api';

function CoverLetterPreview({ letter, formData, onReset }) {
  const [copied, setCopied] = useState(false);
  const [isExporting, setIsExporting] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(letter.cover_letter);
    setCopied(true);
    toast.success('Copied to clipboard!');
    setTimeout(() => setCopied(false), 2000);
  };

  const handleExport = async (format) => {
    setIsExporting(true);
    
    try {
      const response = await coverLetterAPI.exportCoverLetter(
        {
          cover_letter: letter.cover_letter,
          applicant_name: formData.applicant_name,
          company_name: formData.company_name,
        },
        format
      );

      // Create download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      
      const filename = response.headers['content-disposition']
        ?.split('filename=')[1]
        ?.replace(/"/g, '') || `cover_letter.${format}`;
      
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
      
      toast.success(`Downloaded as ${format.toUpperCase()}!`);
    } catch (error) {
      console.error('Export error:', error);
      toast.error('Failed to export. Please try again.');
    } finally {
      setIsExporting(false);
    }
  };

  return (
    <div className="space-y-6 animate-slide-up">
      {/* Stats Bar */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-white rounded-lg p-4 shadow-md">
          <div className="text-2xl font-bold text-primary-600">
            {letter.word_count}
          </div>
          <div className="text-sm text-gray-600">Words</div>
        </div>
        
        <div className="bg-white rounded-lg p-4 shadow-md">
          <div className="text-2xl font-bold text-green-600">
            {letter.generation_time}s
          </div>
          <div className="text-sm text-gray-600">Generation Time</div>
        </div>
        
        <div className="bg-white rounded-lg p-4 shadow-md">
          <div className="text-2xl font-bold text-purple-600 capitalize">
            {letter.ai_provider_used}
          </div>
          <div className="text-sm text-gray-600">AI Provider</div>
        </div>
        
        <div className="bg-white rounded-lg p-4 shadow-md">
          <div className="text-2xl font-bold text-orange-600">
            {letter.matched_keywords.length}
          </div>
          <div className="text-sm text-gray-600">Keywords Matched</div>
        </div>
      </div>

      {/* Matched Keywords */}
      {letter.matched_keywords.length > 0 && (
        <div className="card">
          <div className="flex items-center space-x-2 mb-3">
            <Tag className="w-5 h-5 text-primary-600" />
            <h3 className="text-lg font-semibold text-gray-900">
              Matched Keywords
            </h3>
          </div>
          <div className="flex flex-wrap gap-2">
            {letter.matched_keywords.map((keyword, index) => (
              <span
                key={index}
                className="px-3 py-1 bg-primary-100 text-primary-700 rounded-full text-sm font-medium"
              >
                {keyword}
              </span>
            ))}
          </div>
        </div>
      )}

      {/* Cover Letter Display */}
      <div className="card">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <FileText className="w-5 h-5 text-primary-600" />
            <h3 className="text-lg font-semibold text-gray-900">
              Your Cover Letter
            </h3>
          </div>
          
          <button
            onClick={handleCopy}
            className="flex items-center space-x-2 px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg transition-colors"
          >
            {copied ? (
              <>
                <Check className="w-4 h-4 text-green-600" />
                <span className="text-sm font-medium text-green-600">Copied!</span>
              </>
            ) : (
              <>
                <Copy className="w-4 h-4 text-gray-700" />
                <span className="text-sm font-medium text-gray-700">Copy</span>
              </>
            )}
          </button>
        </div>
        
        <div className="prose max-w-none">
          <div className="bg-gray-50 rounded-lg p-6 border border-gray-200 whitespace-pre-wrap font-serif text-gray-800 leading-relaxed">
            {letter.cover_letter}
          </div>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex flex-wrap gap-4 justify-center">
        <button
          onClick={() => handleExport('pdf')}
          disabled={isExporting}
          className="btn-primary flex items-center space-x-2"
        >
          <Download className="w-4 h-4" />
          <span>Download PDF</span>
        </button>
        
        <button
          onClick={() => handleExport('docx')}
          disabled={isExporting}
          className="btn-primary flex items-center space-x-2"
        >
          <Download className="w-4 h-4" />
          <span>Download DOCX</span>
        </button>
        
        <button
          onClick={() => handleExport('txt')}
          disabled={isExporting}
          className="btn-secondary flex items-center space-x-2"
        >
          <Download className="w-4 h-4" />
          <span>Download TXT</span>
        </button>
        
        <button
          onClick={onReset}
          className="btn-secondary flex items-center space-x-2"
        >
          <RotateCcw className="w-4 h-4" />
          <span>Create New</span>
        </button>
      </div>
    </div>
  );
}

export default CoverLetterPreview;

