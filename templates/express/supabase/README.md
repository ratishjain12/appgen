# Express.js with Supabase

This template provides a complete Express.js setup with Supabase database integration, including real-time features.

## Features

- ✅ Express.js server with security middleware
- ✅ Supabase database integration
- ✅ User model with CRUD operations
- ✅ Real-time capabilities
- ✅ Environment variable configuration
- ✅ CORS enabled
- ✅ Helmet security headers
- ✅ Morgan logging

## Quick Start

1. **Install dependencies:**

   ```bash
   npm install
   ```

2. **Set up Supabase:**

   - Go to [Supabase Dashboard](https://supabase.com/dashboard)
   - Create a new project
   - Go to Settings > API
   - Copy your project URL and anon key

3. **Set up environment variables:**

   ```bash
   cp env.example .env
   # Edit .env with your Supabase credentials
   ```

4. **Create the users table in Supabase:**

   ```sql
   CREATE TABLE users (
     id SERIAL PRIMARY KEY,
     name VARCHAR NOT NULL,
     email VARCHAR UNIQUE NOT NULL,
     created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
     updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
   );
   ```

5. **Start the server:**

   ```bash
   # Development mode
   npm run dev

   # Production mode
   npm start
   ```

## API Endpoints

- `GET /` - Health check
- `GET /api/users` - Get all users
- `POST /api/users` - Create a new user
- `GET /api/users/:id` - Get user by ID
- `PUT /api/users/:id` - Update user
- `DELETE /api/users/:id` - Delete user
- `GET /api/users/realtime` - Real-time endpoint info

## Real-time Features

Supabase provides real-time capabilities out of the box. To use real-time features in your frontend:

```javascript
// Frontend example
import { createClient } from "@supabase/supabase-js";

const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// Subscribe to real-time changes
const subscription = supabase
  .channel("users")
  .on(
    "postgres_changes",
    { event: "*", schema: "public", table: "users" },
    (payload) => {
      console.log("Change received!", payload);
    }
  )
  .subscribe();
```

## Environment Variables

| Variable            | Description               | Required           |
| ------------------- | ------------------------- | ------------------ |
| `PORT`              | Server port               | No (default: 3000) |
| `SUPABASE_URL`      | Your Supabase project URL | Yes                |
| `SUPABASE_ANON_KEY` | Your Supabase anon key    | Yes                |

## Database Configuration

The application uses Supabase, which is built on PostgreSQL. Supabase provides:

- Automatic API generation
- Real-time subscriptions
- Row Level Security (RLS)
- Built-in authentication
- Database backups

## Adding New Tables

To add new tables, create them in the Supabase dashboard or use the SQL editor:

```sql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Row Level Security (RLS)

Supabase includes Row Level Security by default. You can enable/disable it per table:

```sql
-- Enable RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Users can view their own data" ON users
  FOR SELECT USING (auth.uid() = id);
```

## Deployment

This template is ready for deployment on platforms like:

- Vercel
- Netlify
- Railway
- Heroku
- DigitalOcean App Platform

Make sure to set the Supabase environment variables in your deployment platform.

## Supabase Features

- **Database**: PostgreSQL with automatic API generation
- **Auth**: Built-in authentication system
- **Storage**: File storage with CDN
- **Edge Functions**: Serverless functions
- **Realtime**: Real-time subscriptions
- **Dashboard**: Web-based database management
