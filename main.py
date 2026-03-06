from fastapi import FastAPI, HTTPException
    from typing import Optional
    from homeharvest import scrape_property
    
    app = FastAPI()
    
    
    def fetch_data(
        location: str,
        listing_type: str,
        limit: int,
        price_min: Optional[int],
        price_max: Optional[int],
        beds_min: Optional[int],
        baths_min: Optional[float],
    ):
        return scrape_property(
            location=location,
            listing_type=listing_type,
            return_type="raw",
            limit=limit,
            extra_property_data=True,
            price_min=price_min,
            price_max=price_max,
            beds_min=beds_min,
            baths_min=baths_min,
        )
    
    
    @app.get("/rentals")
    def rentals(
        location: str,
        listingType: str = "for_rent",
        limit: int = 200,
        priceMin: Optional[int] = None,
        priceMax: Optional[int] = None,
        bedsMin: Optional[int] = None,
        bathsMin: Optional[float] = None,
    ):
        try:
            return fetch_data(
                location=location,
                listing_type=listingType,
                limit=limit,
                price_min=priceMin,
                price_max=priceMax,
                beds_min=bedsMin,
                baths_min=bathsMin,
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
    
    
    @app.get("/agents")
    def agents(
        location: str,
        listingType: str = "for_sale",
        limit: int = 200,
    ):
        try:
            return fetch_data(
                location=location,
                listing_type=listingType,
                limit=limit,
                price_min=None,
                price_max=None,
                beds_min=None,
                baths_min=None,
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
    
