#!/bin/bash

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 Checking Application Status..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check Backend
if curl -s http://localhost:8000/api/health > /dev/null 2>&1; then
    echo "✅ Backend:  RUNNING on http://localhost:8000"
else
    echo "❌ Backend:  NOT RUNNING"
fi

# Check Frontend
if curl -s http://localhost:5173 > /dev/null 2>&1; then
    echo "✅ Frontend: RUNNING on http://localhost:5173"
else
    echo "❌ Frontend: NOT RUNNING"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Open: http://localhost:5173"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
