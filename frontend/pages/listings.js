export async function getServerSideProps() {
  const base = process.env.API_INTERNAL_URL || process.env.NEXT_PUBLIC_API_BASE_URL || 'http://backend:8000'
  const res = await fetch(`${base}/listings?limit=100`).catch(() => null)
  const listings = res && res.ok ? await res.json() : []
  return { props: { listings } }
}

export default function ListingsPage({ listings }) {
  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h1>Listings ({listings.length})</h1>
      <ul>
        {listings.map((l) => (
          <li key={l.id}>
            {l.brand} {l.model} {l.year || ''} — R$ {l.price_brl ?? '-'} [{l.status}]
          </li>
        ))}
      </ul>
    </main>
  )
}
