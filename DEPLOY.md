# Deploy Guide - Render.com

## Prerequisites

### Test locally
```bash
reflex run
```

### Push to GitHub
```bash
git add .
git commit -m "Deploy setup"
git push origin main
```

## Deployment Steps

### Option A: Automatic (via render.yaml)

1. Login to https://render.com with GitHub
2. Click **New** → **Blueprint**
3. Select repository: `GoldSight-Reflex-GUI`
4. Click **Apply** (auto-reads render.yaml)
5. Wait ~5-10 minutes for build
6. Access: `https://goldsight-reflex-gui.onrender.com`

### Option B: Manual Configuration

1. **New Web Service** on Render
2. Connect GitHub repository
3. Configure:
   - **Name:** `goldsight-reflex-gui`
   - **Region:** Singapore
   - **Runtime:** Python 3
   - **Build Command:**
     ```bash
     pip install --upgrade pip && pip install -r requirements.txt && reflex init && reflex export --frontend-only
     ```
   - **Start Command:**
     ```bash
     reflex run --env prod --backend-only
     ```
   - **Environment Variables:**
     ```
     PYTHON_VERSION=3.11.9
     ```

## Troubleshooting

### Build Failed - Module Not Found

**Solution:**
```bash
pip install -r requirements.txt
reflex init
reflex export
```

### Frontend Export Failed

**Solution:**
- Check build logs on Render dashboard
- Ensure Node.js >= 18
- Try with debug:
  ```bash
  reflex init && reflex export --frontend-only --loglevel debug
  ```

### 502 Bad Gateway

**Solution:**
- Check start command
- Verify port binding (Render auto-sets PORT env var)
- Enable debug mode:
  ```bash
  reflex run --env prod --backend-only --loglevel debug
  ```

### Missing Cache Data

**Solution:**
```bash
git add goldsight/data/cache/*.json
git commit -m "Add cached charts"
git push
```

## Production Optimization

### Auto-Deploy
Render auto-redeploys on:
- Push to `main` branch
- Pull request merge

Disable: **Settings** → **Auto-Deploy** → OFF

### Custom Domain
1. **Settings** → **Custom Domain**
2. Add domain
3. Update DNS records per Render instructions

## Monitoring

**Logs:** Dashboard → Service → Logs (Build/Deploy/Runtime)

**Metrics:** CPU, Memory, Request count, Response time

## Free Tier Limits

- 750 hours/month
- 512MB RAM
- Auto-sleep after 15 min inactivity
- ~30s cold start

Upgrade to Starter ($7/mo) for always-on service
