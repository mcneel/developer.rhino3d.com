+++
aliases = ["/en/5/guides/cpp/tracking-camera-changes-with-conduits/", "/en/6/guides/cpp/tracking-camera-changes-with-conduits/", "/en/7/guides/cpp/tracking-camera-changes-with-conduits/", "/wip/guides/cpp/tracking-camera-changes-with-conduits/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to use a conduit that uses notifiers to track camera information using C/C++."
keywords = [ "rhino", "camera", "conduit" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Tracking Camera Changes with Conduits"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/trackcamera"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Problem

How can you get a windows message from Rhino viewport, specifically when rotating some object in viewport with right click?  The goal is to get the parameters from the camera viewport when there is an event, like mouse move or right click.  You need those camera settings parameters so that you can set them in another view.

## Solution

This can be done through what is called a Conduit Notification.  Basically, you setup a `CRhinoDisplayConduit`, attach it to a specific viewport (or all), and then "listen" for specific notifications by overriding `CRhinoDisplayConduit::NotifyConduit`.  You would most likely be interested in `CN_PIPELINEOPENED`, `CN_PIPELINECLOSED`, and `CN_PROJECTIONCHANGED` events.  On those events you can query the current viewport (camera) for any settings you want, and then react accordingly.

## Sample

The following sample plugin command demonstrates a conduit that uses notifiers to track camera information.  It also demonstrates how to create a HUD (Heads Up Display) used to display the tracked results and overlay them onto the viewport using transparent bitmap drawing.

```cpp
#include "stdafx.h"

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
//
// BEGIN TestCameraTracker command
//
class CCameraTrackingConduit : public CRhinoDisplayConduit
{
public:
              CCameraTrackingConduit();

  bool        ExecConduit(
                  CRhinoDisplayPipeline&, // pipeline executing this conduit
                  UINT,                   // current channel within the pipeline
                  bool&                   // channel termination flag
                  );  

  void        NotifyConduit(EConduitNotifiers, CRhinoDisplayPipeline&);

public:
  void        StartTracking(const CRhinoView*);
  void        StopTracking(void);

// Conduit specific attributes...
public:
  ON_3dPoint    m_CameraLocation;
  ON_3dVector   m_CameraDirection;
  ON_3dPoint    m_CameraTarget;
  double        m_CameraLensLength;
  double        m_CameraNear;
  double        m_CameraFar;

  // TODO: Place more tracking variables here based on what you want to track...

private:
  static const COLORREF m_TransColor = RGB(255,0,255);

  CRhinoUiDib   m_HUD;

  void CreateHUD(const CRhinoDisplayPipeline*);
  bool BuildHUD(void);

};

/////////////////////////////////////////////////////////////////////////////
//
CCameraTrackingConduit::CCameraTrackingConduit()

 : CRhinoDisplayConduit( CSupportChannels::SC_CALCBOUNDINGBOX |
                         CSupportChannels::SC_POSTPROCESSFRAMEBUFFER )
{
}

/////////////////////////////////////////////////////////////////////////////
//
void CCameraTrackingConduit::CreateHUD(const CRhinoDisplayPipeline* dp)
{
  if ( dp != NULL )
  {
    CSize fs = dp->GetFrameSize();

    m_HUD.CreateDib( fs.cx, fs.cy, 32, true );
  }
}

/////////////////////////////////////////////////////////////////////////////
//
bool CCameraTrackingConduit::BuildHUD(void)
{
  LPBYTE    HudBits = m_HUD.FindDIBBits();
  bool      success = false;

  if ( HudBits != NULL )
  {
    CDC*  pDC = m_HUD; // Our HUD is both a bitmap and a GDI device context,
                       // so we can use GDI routines to draw to it (ie. Text operations)

    // Fill entire HUD with transparent color...we only want what we're about
    // to write into the HUD to show up...everything else is transparent so that
    // we can just overlay it onto the frame buffer...hence, it's a HUD (Heads Up Display)
    pDC->FillSolidRect( 0, 0, m_HUD.Width(), m_HUD.Height(), m_TransColor );

    ON_wString    text;
    CSize         exts;
    int           nW = m_HUD.Width();
    int           nH = m_HUD.Height();

    pDC->SetTextColor( RGB( 255, 0, 0 ) );
    pDC->SetBkMode( TRANSPARENT );

    text.Format( "Camera Location: %5.3f, %5.3f, %5.3f", m_CameraLocation.x, m_CameraLocation.y, m_CameraLocation.z );
    exts = pDC->GetTextExtent( text.Array(), text.Length() );
    pDC->TextOut( nW - exts.cx - 5, exts.cy, text.Array(), text.Length() );

    text.Format( "Camera Direction: %5.3f, %5.3f, %5.3f", m_CameraDirection.x, m_CameraDirection.y, m_CameraDirection.z );
    exts = pDC->GetTextExtent( text.Array(), text.Length() );
    pDC->TextOut( nW - exts.cx - 5, exts.cy*2, text.Array(), text.Length() );

    text.Format( "Camera Target: %5.3f, %5.3f, %5.3f", m_CameraTarget.x, m_CameraTarget.y, m_CameraTarget.z );
    exts = pDC->GetTextExtent( text.Array(), text.Length() );
    pDC->TextOut( nW - exts.cx - 5, exts.cy*3, text.Array(), text.Length() );

    text.Format( "Lens Length: %5.3f", m_CameraLensLength );
    exts = pDC->GetTextExtent( text.Array(), text.Length() );
    pDC->TextOut( nW - exts.cx - 5, exts.cy*4, text.Array(), text.Length() );

    text.Format( "Camera Near & Far: %5.3f, %5.3f",m_CameraNear, m_CameraFar );
    exts = pDC->GetTextExtent( text.Array(), text.Length() );
    pDC->TextOut( nW - exts.cx - 5, exts.cy*5, text.Array(), text.Length() );

    // Debugging...check to see what's in HUD by pasting into someting like
    // PhotoShop afte the next line is executed...
    //m_HUD.CopyToClipboard( NULL );

    success = true;
  }

  return success;
}

/////////////////////////////////////////////////////////////////////////////
//
bool CCameraTrackingConduit::ExecConduit(CRhinoDisplayPipeline&    dp,
                                         UINT                      nChannel,
                                         bool&                     bTerminate)
{
  // Is this is not viewport/pipeline we're currently tracking, then bail out now ...
  if ( !IsBound( dp ) )
    return true;

  switch ( nChannel )
  {
    // You might want to track the scene's current extents...or something similar...
    case CSupportChannels::SC_CALCBOUNDINGBOX:
    {
      break;
    }

    // The tracking is conveyed via a Heads Up Display that gets overlaid onto
    // the frame buffer. This channel either let's us replace the frame buffer
    // entirely, or simply modify it in some form...We're just going to build
    // up our HUD and then draw/overlay it on top of the current frame buffer
    // via transparent bitmap drawing...
    case CSupportChannels::SC_POSTPROCESSFRAMEBUFFER:
    {
      if ( BuildHUD() )
      {
        dp.PushDepthTesting( false );
        dp.DrawBitmap( m_HUD, 0, 0, m_TransColor );
        dp.PopDepthTesting();
      }
      break;
    }
  }

  return true;
}

/////////////////////////////////////////////////////////////////////////////
//
void CCameraTrackingConduit::NotifyConduit(EConduitNotifiers       Notify,
                                           CRhinoDisplayPipeline&  dp)
{
  // This conduit notifier only acts on existing pipelines, and assumes they're
  // created and exist...some notify events are based on pipelines coming online
  // and being deleted...so if we don't do the following, then we cannot assume
  // the current pipeline or any of its members are valid (without more checking).
  // Since we're only interested in a few events, we filter on them here...
  //
  // Note: If you want to process/handle other types of notification events, then
  //       make sure you add them to the condition below...
  if ( (Notify != CN_FRAMESIZECHANGED)  &&
       (Notify != CN_PROJECTIONCHANGED) &&
       (Notify != CN_PIPELINECLOSED)    &&
       (Notify != CN_PIPELINEDELETED) )
    return;

  const CRhinoViewport&   View = dp.GetRhinoVP(); // We might need specifics from each
  const ON_Viewport&      vp   = View.VP();       // one of these, so we assign them to
                                                  // their own variable for simplicity...

  // Is this the viewport we're currently tracking? ...
  if ( IsBound( dp ) )
  {
    switch ( Notify )
    {
      // Since our HUD's size mirrors the size of the view we're tracking, we need
      // adjust our HUD if/when the view's frame size changes.
      case CN_FRAMESIZECHANGED:
      {
        CreateHUD( &dp );
        break;
      }

      // Something changed the tracked view's projection, camera, or frustum settings...so
      // update our tracking variables accordingly.
      // Note: This only occurs when the view is being manipulated and NOT because some piece
      //       of code somewhere changed a setting. This notification only occurs during frame
      //       updates.
      case CN_PROJECTIONCHANGED:
      {
        m_CameraLocation   = vp.CameraLocation();
        m_CameraDirection  = vp.CameraDirection();
        m_CameraTarget     = vp.TargetPoint();
        m_CameraNear       = vp.FrustumNear();
        m_CameraFar        = vp.FrustumFar();
        vp.GetCamera35mmLensLength( &m_CameraLensLength );

        // TODO: Assign more tracking variables here based on what you want to track...

        break;
      }

      // Not sure what you might want to do here, but this notification happens at the
      // END of EVERY frame update...which tends to be a good place to put/do certain things...
      // Note: The pipeline is closed by the time you receive this event, so writing anything
      //       to the display at this point is out of the question...
      case CN_PIPELINECLOSED:
      {
        break;
      }

      // The pipeline/view we're tracking just got deleted...so we need to
      // stop tracking it...
      // Note: This can happen either because the view was deleted, the file was closed,
      //       or the display mode was changed to one that uses a different type of pipeline.
      //       Since it's hard to distinguish between all of those, we'll just disable ourself
      //       and error on the side of being safe.
      case CN_PIPELINEDELETED:
      {
        StopTracking();
        break;
      }
    }  
  }
}

/////////////////////////////////////////////////////////////////////////////
//
void CCameraTrackingConduit::StartTracking(const CRhinoView* pView)
{
  if ( pView != NULL )
  {
    const ON_Viewport&   vp = pView->Viewport().VP();

    CreateHUD( pView->DisplayPipeline() );

    Bind( vp );
    Enable();
  }
}

/////////////////////////////////////////////////////////////////////////////
//
void CCameraTrackingConduit::StopTracking()
{
  UnbindAll();
  Disable();
}

#pragma region TestCameraTracker command

class CCommandTestCameraTracker : public CRhinoCommand
{
public:
	CCommandTestCameraTracker() {}
	~CCommandTestCameraTracker() {}
	UUID CommandUUID()
	{
		// {3D16E807-F816-4C86-92A2-C7B40C883E03}
		static const GUID TestCameraTrackerCommand_UUID =
		{ 0x3D16E807, 0xF816, 0x4C86, { 0x92, 0xA2, 0xC7, 0xB4, 0x0C, 0x88, 0x3E, 0x03 } };
		return TestCameraTrackerCommand_UUID;
	}
	const wchar_t* EnglishCommandName() { return L"TestCameraTracker"; }
	CRhinoCommand::result RunCommand( const CRhinoCommandContext& );

public:
  CCameraTrackingConduit  m_Conduit;

};

// The one and only CCommandTestCameraTracker object
static class CCommandTestCameraTracker theTestCameraTrackerCommand;

CRhinoCommand::result CCommandTestCameraTracker::RunCommand( const CRhinoCommandContext& context )
{
  // Are we already tracking a view? ...
  if ( !m_Conduit.IsEnabled() )
  {
    // No, so start tracking the active viewport...
    CRhinoView* pActiveView = ::RhinoApp().ActiveView();

    if ( pActiveView != NULL )
    {
      m_Conduit.StartTracking( pActiveView ); // Only track the camera of a single, specific view...
    }
  }
  else
    // We're already tracking something so stop...this makes the command act as a toggle.
    m_Conduit.StopTracking();

  // Force redraw of all views...
  context.m_doc.Regen();

	return CRhinoCommand::success;
}

#pragma endregion

//
// END TestCameraTracker command
//
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
```
