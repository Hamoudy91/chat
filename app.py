# Deploying TCL Chatbot Using Vercel (Free)

## Prerequisites
1. Node.js installed on your computer
2. Git installed on your computer
3. GitHub account
4. Vercel account (free signup at vercel.com)

## Step 1: Create a New React Project

```bash
# Create a new Next.js project with TypeScript
npx create-next-app@latest tcl-chatbot --typescript --tailwind --eslint

# Navigate to the project directory
cd tcl-chatbot
```

## Step 2: Install Required Dependencies

```bash
npm install lucide-react
```

## Step 3: Set Up Project Structure

1. Create a new components folder:
```bash
mkdir src/components
```

2. Create the ChatBot component file:
```bash
touch src/components/ChatBot.tsx
```

3. Copy the provided ChatBot component code into `src/components/ChatBot.tsx`

4. Update `src/app/page.tsx`:
```typescript
import ChatBot from '@/components/ChatBot'

export default function Home() {
  return (
    <main className="min-h-screen p-4 bg-gray-100">
      <ChatBot />
    </main>
  )
}
```

## Step 4: Push to GitHub

1. Create a new repository on GitHub

2. Initialize and push your project:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/tcl-chatbot.git
git push -u origin main
```

## Step 5: Deploy on Vercel

1. Go to [vercel.com](https://vercel.com) and sign up/login
2. Click "New Project"
3. Import your GitHub repository
4. Keep the default settings and click "Deploy"

Vercel will automatically build and deploy your project. Once complete, you'll get a URL where your chatbot is live (e.g., `https://tcl-chatbot.vercel.app`).

## Additional Notes

- Vercel's free tier includes:
  - Unlimited personal projects
  - Automatic HTTPS
  - Continuous deployment from GitHub
  - Global CDN
  - Analytics

- To update your deployed app:
  1. Make changes locally
  2. Commit and push to GitHub
  3. Vercel will automatically redeploy

## Alternative Free Hosting Options

1. **GitHub Pages**
   - Free hosting for static sites
   - Requires slight configuration for React apps

2. **Netlify**
   - Similar to Vercel
   - Generous free tier
   - Easy deployment from Git

3. **Render**
   - Modern platform with free static site hosting
   - Simple deployment process

## Troubleshooting

If you encounter issues:
1. Check your browser console for errors
2. Verify all dependencies are installed
3. Ensure all imports are correct
4. Check Vercel's deployment logs

For local development, use:
```bash
npm run dev
```
