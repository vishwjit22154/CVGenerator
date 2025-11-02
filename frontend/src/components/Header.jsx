import { FileText } from 'lucide-react';

function Header() {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center space-x-3">
          <div className="bg-primary-600 p-2 rounded-lg">
            <FileText className="w-6 h-6 text-white" />
          </div>
          <h1 className="text-2xl font-bold text-gray-900">
            AI Cover Letter Generator
          </h1>
        </div>
      </div>
    </header>
  );
}

export default Header;

